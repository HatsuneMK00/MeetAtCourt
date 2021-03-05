# -*- coding: utf-8 -*-

# 处理球类资产相关请求

from flask import Blueprint

equipment = Blueprint("equipment", __name__)


@equipment.route("/")
def test():
    return "<h1>test from equipment</h1>"