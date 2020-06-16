"""
蓝图
"""
from . import *


@index_blu.route('/index')
def index():
    return 'index'
