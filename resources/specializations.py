import uuid
from flask import abort, request
from flask_smorest import Blueprint
from flask.views import MethodView
from db import specializations
from schemas import SpecializationSchema

blp = Blueprint("specialization", __name__, description="Operations on specialization")

@blp.route("/specialization/<string:specialization_id>")
class Specialization(MethodView):
    def get(self, specialization_id):
        try:
            return specializations[specialization_id]
        except KeyError:
            abort(404, message="Specialization not found.")
    def delete(self, specialization_id):
        try:
            del specializations[specialization_id]
            return {"message": "Specialization deleted."}
        except KeyError:
            abort(404, message="Specialization not found.")


@blp.route("/specialization")
class SpecializationList(MethodView):
    def get(self):
        return {"specializations": list(specializations.values())}

    @blp.arguments(SpecializationSchema)
    def post(self, specialization_data):
        specialization_id = uuid.uuid4().hex
        specialization = {**specialization_data, "id": specialization_id}
        specializations[specialization_id] = specialization
        return specialization