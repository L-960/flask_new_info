from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import Config

app = Flask(__name__)

# 导入配置
app.config.from_object(Config)
# 数据库要和app关联
db = SQLAlchemy(app)
# 初始化redis配置(Strict:严格的)
# redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf保护，只用于服务器验证功能
CSRFProtect(app)
# 设置session保存指定位置
Session(app)


@app.route('/')
def index():
    session['name'] = '吕星宇'
    return 'index'
