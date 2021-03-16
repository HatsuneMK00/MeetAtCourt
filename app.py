# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api, Resource

from biz.equipment import equipment
from biz.yueqiu import yueqiu
from biz.member import member

app = Flask(__name__)
app.register_blueprint(yueqiu, url_prefix="/yueqiu")
app.register_blueprint(member, url_prefix="/member")
app.register_blueprint(equipment, url_prefix="/equipment")

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run()
