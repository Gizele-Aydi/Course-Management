from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import CourseItemModel
from schemas import CourseItemSchema, CourseItemUpdateSchema

blp = Blueprint("CourseItems", "courseitems", description="Operations on course items")

@blp.route("/courseitem/<string:courseitem_id>")
class CourseItem(MethodView):
    @blp.response(200, CourseItemSchema)
    def get(self, courseitem_id):
        courseitem = CourseItemModel.query.get_or_404(courseitem_id)
        return courseitem

    def delete(self, courseitem_id):
        courseitem = CourseItemModel.query.get_or_404(courseitem_id)
        db.session.delete(courseitem)
        db.session.commit()
        return {"message": "CourseItem deleted."}

    @blp.arguments(CourseItemUpdateSchema)

    @blp.response(200, CourseItemSchema)

    def put(self, courseitem_data, courseitem_id):
        courseitem = CourseItemModel.query.get(courseitem_id)
        if courseitem:
            courseitem.type = courseitem_data["type"]
            courseitem.name = courseitem_data["name"]
        else:
            courseitem = CourseItemModel(id=courseitem_id, **courseitem_data)
        db.session.add(courseitem)
        db.session.commit()
        return courseitem

@blp.route("/courseitem")
class CourseItemList(MethodView):

    @blp.response(200, CourseItemSchema(many=True))
    def get(self):
        return CourseItemModel.query.all()

    @blp.arguments(CourseItemSchema)

    @blp.response(201, CourseItemSchema)

    def post(self, courseitem_data):
        courseitem = CourseItemModel(**courseitem_data)
        try:
            db.session.add(courseitem)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the course item.")
        return courseitem