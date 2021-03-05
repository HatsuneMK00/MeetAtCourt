# -*- coding: utf-8 -*-

# 处理用户相关请求

from flask import Blueprint

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/")
def test():
    return "<h1>test from user</h1>"