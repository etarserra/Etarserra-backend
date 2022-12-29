from app.models import BaseModel
from app.extensions import db
from app.association import associationAuthorFile, associationTagFile, associationCategoryFile, associationAreaFile
from datetime import datetime

class File(BaseModel):
    __tablename__ = "file"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creationTimeStamp = db.Column(db.DateTime, default=datetime.now())
    media_path = db.Column(db.String(300))
    type = db.Column(db.String(100))
    click_quantity = db.Column(db.Integer)
    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    awarded = db.Column(db.String(100))
    description = db.Column(db.String(1000))

    authors_associated = db.relationship("Author", secondary=associationAuthorFile, backref='files')
    tags_associated = db.relationship("Tag", secondary=associationTagFile, backref='files')
    categories_associated = db.relationship("Category", secondary=associationCategoryFile, backref='files')
    areas_associated = db.relationship("Area", secondary=associationAreaFile, backref='files')
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
