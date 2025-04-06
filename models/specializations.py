from db import db

class SpecializationModel(db.Model):
    __tablename__ = 'specializations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    courseitems = db.relationship('CourseItemModel', back_populates='specialization', lazy="dynamic", cascade="all, delete")
