from app.extensions import db, ma, migrate, jwt, mail, cors
from app.config import Config
from flask import Flask


from app.storages.routes import storage_api
from app.banner.routes import banner_api
from app.author.routes import author_api
from app.tag.routes import tag_api
from app.auth.routes import auth_api
from app.user.routes import user_api
from app.file.routes import file_api
from app.category.routes import category_api
from app.area.routes import area_api


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app, resources={r"/*":{"origins": "*"}})
    migrate.init_app(app, db)


    app.register_blueprint(file_api)
    app.register_blueprint(storage_api)
    app.register_blueprint(banner_api)
    app.register_blueprint(tag_api)
    app.register_blueprint(author_api)
    app.register_blueprint(auth_api)
    app.register_blueprint(user_api)
    app.register_blueprint(category_api)
    app.register_blueprint(area_api)

    
    return app