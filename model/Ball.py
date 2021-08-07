# -*- coding: utf-8 -*-
# created by makise, 2021/3/17
from flask_restful import fields


class Ball:
    def __init__(self, ball_id, ball_type, member_id, ball_brand):
        self.ball_id = ball_id
        self.ball_type = ball_type
        self.member_id = member_id
        self.ball_brand = ball_brand


resource_field_ball = {
    'ball_id': fields.Integer,
    'ball_type': fields.String,
    'member_id': fields.String,
    'ball_brand': fields.String
}