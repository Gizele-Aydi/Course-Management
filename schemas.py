from marshmallow import Schema, fields

class CourseItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Float(required=True)
    specialization_id = fields.Str(required=True)

class CourseItemUpdateSchema(Schema):
    name = fields.Str()
    type = fields.Float()

class SpecializationSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)