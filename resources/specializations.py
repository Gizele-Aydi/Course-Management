from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import SpecializationModel
from schemas import SpecializationSchema

blp = Blueprint("Specializations", "specializations", description="Operations on specializations")

@blp.route("/specialization/<string:specialization_id>")
class Specialization(MethodView):
    @blp.response(200, SpecializationSchema)
    def get(self, specialization_id):
        specialization = SpecializationModel.query.get_or_404(specialization_id)
        return specialization

    def delete(self, specialization_id):
        specialization = SpecializationModel.query.get_or_404(specialization_id)
        db.session.delete(specialization)
        db.session.commit()
        return {"message": "Specialization deleted"}, 200


@blp.route("/specialization")
class SpecializationList(MethodView):
    @blp.response(200, SpecializationSchema(many=True))
    def get(self):
        return SpecializationModel.query.all()

    @blp.arguments(SpecializationSchema)

    @blp.response(201, SpecializationSchema)

    def post(self, specialization_data):
        specialization = SpecializationModel(**specialization_data)
        try:
            db.session.add(specialization)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A specialization with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the specialization.")
        return specialization