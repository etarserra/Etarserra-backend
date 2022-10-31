from app.models import BaseModel
from app.extensions import db

class Banner(BaseModel):
    __tablename__ = "banner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    banner_name = db.Column(db.String(300))
    media_path = db.Column(db.String(300))
