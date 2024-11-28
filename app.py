from flask_smorest import Api
from flask import Flask, request, abort
from resources.course_items import blp as Course_item_Blueprint
from resources.specializations import blp as Specialization_Blueprint
app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"]=True
app.config["API_TITLE"]="TBS REST API"
app.config["API_VERSION"]="RELEASE 1"
app.config["OPENAPI_VERSION"]="3.0.3"
app.config["OPENAPI_URL_PREFIX"]="/"
app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
api=Api(app)
api.register_blueprint(Course_item_Blueprint)
api.register_blueprint(Specialization_Blueprint)