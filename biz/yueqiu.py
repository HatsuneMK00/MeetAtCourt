# -*- coding: utf-8 -*-

# 处理约球相关请求
# 所有/yueqiu开头的url会路由到本文件内
# add_resource时忽略/yueqiu前缀
# 例如：/yueqiu/volleyball 直接写/volleyball

from flask import Blueprint
from flask_restful import Api, Resource, marshal_with
from dao.yueqiu_mapper import *

from model.YueQiu import resource_field_yueqiu

yueqiu = Blueprint("yueqiu", __name__)
api_reserve = Api(yueqiu)


# 批量获取约球信息
class YueQiuInfo(Resource):
    @marshal_with(resource_field_yueqiu)
    def get(self, offset):
        # 传参时 *一定要使用字典形式传参*
        result = select_ten_item_from_offset(offset=offset)
        return result


api_reserve.add_resource(YueQiuInfo, '/offset/<int:offset>')
