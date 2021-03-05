# -*- coding: utf-8 -*-

# 处理约球相关请求

from flask import Blueprint

reserve = Blueprint("reserve", __name__)


@reserve.route("/")
def test():
    return "<h1>test from reserve</h1>"
