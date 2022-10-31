from app.extensions import db

# Tabela de associacao de autor com arquivo
associationAuthorFile = db.Table("authorship", db.Model.metadata,
                                    db.Column("author_id", db.Integer, db.ForeignKey("author.id")),
                                    db.Column("file_id", db.Integer, db.ForeignKey("file.id")))

# Tabela de associacao de tag com arquivo
associationTagFile = db.Table("file_tag", db.Model.metadata,
                                    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
                                    db.Column("file_id", db.Integer, db.ForeignKey("file.id")))

# Tabela de associacao de categoria com arquivo
associationCategoryFile = db.Table("file_category", db.Model.metadata,
                                    db.Column("category_id", db.Integer, db.ForeignKey("category.id")),
                                    db.Column("file_id", db.Integer, db.ForeignKey("file.id")))

# Tabela de associacao de area com arquivo
associationAreaFile = db.Table("file_area", db.Model.metadata,
                                    db.Column("area_id", db.Integer, db.ForeignKey("area.id")),
                                    db.Column("file_id", db.Integer, db.ForeignKey("file.id")))