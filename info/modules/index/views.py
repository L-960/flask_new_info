"""
蓝图
"""
from flask import render_template, current_app

# 导入创建的蓝图，在views中编写路由和函数
from . import index_blu


@index_blu.route('/')
def index():
    return render_template('news/index.html')


@index_blu.route('/favicon.ico')
def get_web_logo():
    return current_app.send_static_file('news/favicon.ico')
