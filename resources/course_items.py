import uuid
from flask import abort
from flask_smorest import Blueprint
from flask.views import MethodView
from db import course_items
from schemas import CourseItemSchema, CourseItemUpdateSchema

blp = Blueprint("Course_items", "course_items", description="Operations on course_items")
@blp.route("/course_item/<string:course_item_id>")
class Course_item(MethodView):
    def get(self, course_item_id):
        try:
            return course_items[course_item_id]
        except KeyError:
            abort(404, message="Course_item not found.")
    def delete(self, course_item_id):
        try:
           del course_items[course_item_id]
           return {"message": "Course_item deleted."}
        except KeyError:
            abort(404, message="Course_item not found.")

    @blp.arguments(CourseitemUpdateSchema)
    def put(self, course_item_data, course_item_id):
        try:
            course_item = course_items[course_item_id]
            course_item |= course_item_data
            return course_item
        except KeyError:
            abort(404, message="Course_item not found.")


@blp.route("/course_item")
class Course_itemList(MethodView):
    def get(self):
        return {"course_items": list(course_items.values())}

    @blp.arguments(CourseitemSchema)
    def post(self, course_item_data):
        course_item_id = uuid.uuid4().hex
        course_item = {**course_item_data, "id": course_item_id}
        course_items[course_item_id] = course_item
        return course_item
