from datetime import datetime

import flask

from fastapi import db, ms


class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class BaseSchema(ms.Schema):
    def jsonify(self, obj, *args, **kwargs):
        data, errors = self.dump(obj, many=self.many)
        if errors:
            resp = {'code': -1, 'msg': 'dump对象失败', 'data': None}
        else:
            resp = {'code': 0, 'msg': '', 'data': data}
        return flask.jsonify(resp, *args, **kwargs)