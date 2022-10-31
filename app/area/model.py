from app.models import BaseModel
from app.extensions import db


# Entidade de area, a ser associada a um arquivo
class Area(BaseModel):
    __tablename__ = "area"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
