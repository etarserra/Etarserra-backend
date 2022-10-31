from app.models import BaseModel
from datetime import datetime
from app.extensions import db
import bcrypt
from app.config import Config


# Entidade de usuario, para tipo "admin" e "colaborador"
class User(BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.LargeBinary(128), nullable=False)
    verificationPinHash = db.Column(db.LargeBinary(128))
    createdPinTimestamp = db.Column(db.DateTime)
    isAdmin = db.Column(db.Boolean(), default=False)
    files_created = db.relationship('File', backref='creator')


    """ Configs senha """
    @property
    def password(self):
        raise AttributeError("Password is not a readable atrribute.")
    
    @password.setter
    def password(self, new_password):
        self.password_hash = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
    
    def verify_password(self, password_received):
        return bcrypt.checkpw(password_received.encode(), self.password_hash)
    

    """ Configs pin de verificacao """
    @property
    def verificationPin(self):
        raise AttributeError("Verification Pin is not a readable atrribute.")
    
    @verificationPin.setter
    def verificationPin(self, verificationPin):
        self.createdPinTimestamp = datetime.now()
        self.verificationPinHash = bcrypt.hashpw(verificationPin.encode(), bcrypt.gensalt())
    
    # Tem 5 minutos pra usar pin
    def verify_pin(self, verificationPinReceived):
        timeDifference = round((datetime.now() - self.createdPinTimestamp).seconds / 60)
        return bcrypt.checkpw(verificationPinReceived.encode(), self.verificationPinHash) and timeDifference <= Config.VALID_VERIFICATION_PIN_TIME
