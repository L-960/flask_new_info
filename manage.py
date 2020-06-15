from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import app, db

# 注册管理flask_script
manage = Manager(app)
# 数据库迁移
Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
