# -*- coding: utf-8 -*-

# 处理约球相关请求
# 所有/yueqiu开头的url会路由到本文件内
# add_resource时忽略/yueqiu前缀
# 例如：/yueqiu/volleyball 直接写/volleyball

from flask import Blueprint
from flask_restful import Api, Resource

yueqiu = Blueprint("reserve", __name__)
api_reserve = Api(yueqiu)


class HelloWorldYueQiu(Resource):
    def get(self):
        return {'hello': 'world yueqiu'}

api_reserve.add_resource(HelloWorldYueQiu, '/')
