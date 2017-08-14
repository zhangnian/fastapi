
class APIError(Exception):
    def __init__(self, ret, msg):
        Exception.__init__(self)
        self.ret = ret
        self.msg = msg

    def to_dict(self):
        return {'code': self.ret, 'msg': self.msg, 'data':{}}


