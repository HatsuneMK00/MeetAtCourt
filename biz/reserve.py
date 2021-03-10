# -*- coding: utf-8 -*-

# 处理约球相关请求
# 所有/reserve开头的url会路由到本文件内
# add_resource时忽略/reserve前缀
# 例如：/reserve/volleyball 直接写/volleyball

from flask import Blueprint
from flask_restful import Api, Resource

reserve = Blueprint("reserve", __name__)
api_reserve = Api(reserve)


class HelloWorldReserve(Resource):
    def get(self):
        return {'hello': 'world reserve'}

api_reserve.add_resource(HelloWorldReserve, '/')
