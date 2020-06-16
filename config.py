import logging

import redis


class Config(object):
    """工程信息配置"""
    DEBUG = True

    # 数据库配置(information:信息)
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/information0615"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True

    SECRET_KEY = "daasdasd"

    # 配置redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session配置信息
    # 指定session保存到redis中
    SESSION_TYPE = 'redis'
    # 让cookie中的session id被加密处理
    SESSION_USE_SIGNER = True
    # 使用redis实例
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置是否使用永久会话
    SESSION_PERMANENT = False
    # 设置过期时间（session有效期）（24小时）
    PERMANENT_SESSION_LIFETIME = 86400

    # 日志级别
    LEVEL = logging.DEBUG


# 开发环境
class DevelopConfig(Config):
    pass


# 生产环境
class ProductConfig(Config):
    DEBUG = False
    LEVEL = logging.ERROR  # 日志级别


# 测试环境
class TestingConfig(Config):
    TESTING = True


# 通过统一的字典进行配置类的访问
config_dict = {
    'develop': DevelopConfig,
    'product': ProductConfig,
    'testing': TestingConfig,
}
