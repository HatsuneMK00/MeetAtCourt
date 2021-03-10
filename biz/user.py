# -*- coding: utf-8 -*-

# 处理用户相关请求
# 所有/user开头的url会路由到本文件内
# add_resource时忽略/user前缀
# 例如：/user/volleyball 直接写/volleyball

from flask import Blueprint
from flask_restful import Api, Resource

user = Blueprint("user", __name__)
api_user = Api(user)


class HelloWorldUser(Resource):
    def get(self):
        return {'hello': 'world user'}

api_user.add_resource(HelloWorldUser, '/')