# -*- coding: utf-8 -*-

# 处理球类资产相关请求
# 所有/equipment开头的url会路由到本文件内
# add_resource时忽略/equipment前缀
# 例如：/equipment/volleyball 直接写/volleyball

from flask import Blueprint
from flask_restful import Api, Resource

equipment = Blueprint("equipment", __name__)
api_equipment = Api(equipment)

class HelloWorldEquipment(Resource):
    def get(self):
        return {'hello': 'world equipment'}

api_equipment.add_resource(HelloWorldEquipment, '/')