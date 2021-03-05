# -*- coding: utf-8 -*-
from flask import Flask

from biz.equipment import equipment
from biz.reserve import reserve
from biz.user import user

app = Flask(__name__)
app.register_blueprint(reserve, url_prefix="/reserve")
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(equipment, url_prefix="/equipment")

@app.route('/')
def hello_world():
    return 'Hello World! From app'


if __name__ == '__main__':
    app.run()
