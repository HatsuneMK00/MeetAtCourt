# -*- coding: utf-8 -*-

# 处理用户相关请求
# 所有/user开头的url会路由到本文件内
# add_resource时忽略/user前缀
# 例如：/user/volleyball 直接写/volleyball

from flask import Blueprint
from flask_restful import Api, Resource, marshal_with

from model.Member import Member, resource_field_member

member = Blueprint("user", __name__)
api_user = Api(member)


class HelloWorldMember(Resource):
    @marshal_with(resource_field_member)
    def get(self):
        return Member(1, 'guo', 'url', '12345')

api_user.add_resource(HelloWorldMember, '/')