# -*- coding: utf-8 -*-
# created by makise, 2021/3/17
from flask_restful import fields


class YueQiu:
    def __init__(self, yueqiu_id, yueqiu_time, yueqiu_location, member_id, have_ball, yueqiu_note):
        self.yueqiu_id = yueqiu_id
        self.yueqiu_time = yueqiu_time
        self.yueqiu_location = yueqiu_location
        self.member_id = member_id
        self.have_ball = have_ball
        self.yueqiu_note = yueqiu_note


resource_field_yueqiu = {
    'yueqiu_id': fields.Integer,
    'yueqiu_time': fields.DateTime,
    'yueqiu_location': fields.String,
    'member_id': fields.Integer,
    'have_ball': fields.Integer,
    'yueqiu_note': fields.String,
}
