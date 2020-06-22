from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from info import create_app, db

# 设置开发模式，创建app
app = create_app('develop')

# 注册管理flask_script
manage = Manager(app)
# 数据库迁移,迁移命令
Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
