from flask import Flask
from flask_smorest import Api

import models
from db import db
from resources.course_items import blp as Course_item_Blueprint
from resources.specializations import blp as Specialization_Blueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "TBS REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)

    api = Api(app)
    with app.app_context():
        db.create_all()
    api.register_blueprint(Course_item_Blueprint)
    api.register_blueprint(Specialization_Blueprint)

    return app