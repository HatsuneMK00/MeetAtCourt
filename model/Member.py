# -*- coding: utf-8 -*-
# created by makise, 2021/3/16
from flask_restful import fields


class Member:
    def __init__(self, member_id, member_name, head, student_id):
        self.member_id = member_id
        self.member_name = member_name
        self.head = head
        self.student_id = student_id

resource_field_member = {
    'member_id': fields.Integer,
    'member_name': fields.String,
    'head': fields.String,
    'student_id': fields.String
}