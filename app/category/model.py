from app.models import BaseModel
from app.extensions import db


# Entidade de categoria, a ser associada a um arquivo
class Category(BaseModel):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
