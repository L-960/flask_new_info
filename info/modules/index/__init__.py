from flask import Blueprint

# 在__init__创建蓝图
index_blu = Blueprint('index', __name__)

# 获取在views中编写的蓝图路由函数
from . import views
