from marshmallow import post_load

from fastapi import db, ms
from fastapi.model.base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    age = db.Column(db.SmallInteger, default=18, nullable=True)

    def __init__(self, **kwargs):
        for attr in self._attrs:
            setattr(self, attr, kwargs.get(attr))

    @property
    def _attrs(self):
        return ['name', 'age']


class UserSchema(ms.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'name', 'age')

    @post_load
    def make_user(self, data):
        return User(**data)


user_schema = UserSchema()
users_schema = UserSchema(many=True)