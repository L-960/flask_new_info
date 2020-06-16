import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_session import Session
from flask_wtf import CSRFProtect
from config import Config, config_dict


def create_app(config_name):
    """通过传入不同的配置名，切换不同的环境"""
    config = config_dict.get(config_name)
    # 设置日志级别
    log_file(config.LEVEL)
    # TODO
    app = Flask(__name__)
    # 导入app配置
    app.config.from_object(Config)
    # 开启csrf保护，只用于服务器验证功能
    CSRFProtect(app)
    # 设置session保存指定位置
    Session(app)
    # 注册蓝图时，导入和注册写在一起
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)
    return app


# 记录日志
def log_file(level):
    # 设置日志的记录等级,常见等级有: DEBUG<INFO<WARING<ERROR
    logging.basicConfig(level=level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
