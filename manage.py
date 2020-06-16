from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from info import create_app

app = create_app('develop')
# 注册管理flask_script
manage = Manager(app)

# 数据库要和app关联
db = SQLAlchemy(app)
# 数据库迁移
Migrate(app, db)
manage.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session['name'] = '吕星宇'
    return 'index'


if __name__ == '__main__':
    manage.run()
