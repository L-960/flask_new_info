from flask import render_template, session, current_app

from info.models import User
from info.modules.news import news_blu


@news_blu.route('/<int:news_id>')
def news_detail(news_id):

    # 在session中获取当前登陆用户的信息
    user_id = session.get('user_id')

    user = None

    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    data = {
        # 如果存在就返回，不存在就返回空
        "user_info": user.to_dict() if user else None,
    }

    return render_template('news/detail.html', data=data)
