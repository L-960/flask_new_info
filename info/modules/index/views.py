"""
蓝图
"""
from flask import render_template, current_app, session, request, jsonify

# 导入创建的蓝图，在views中编写路由和函数
# from info.models import User
from info import constants
from info.models import User, News, Category
from info.utils.response_code import RET
from . import index_blu


@index_blu.route('/')
def index():
    """首页显示"""
    # 在session中获取当前登陆用户的信息
    user_id = session.get('user_id')

    user = None

    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    try:
        # order_by desc降序查询，limit限制查询结果
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    click_news_list = []

    for news in news_list if news_list else []:
        click_news_list.append(news.to_basic_dict())

    # 获取新闻分类数据
    categories_dicts = []
    categories = Category.query.all()
    for category in categories:
        categories_dicts.append(category.to_dict())

    data = {
        # 如果存在就返回，不存在就返回空
        "user_info": user.to_dict() if user else None,
        "click_news_list": click_news_list,
        'categories': categories_dicts,
    }
    return render_template('news/index.html', data=data)


@index_blu.route('/newslist')
def get_news_list():
    # 获取参数
    args_dict = request.args
    # 第几页
    page = args_dict.get('p', 1)
    # 一页多少数据
    per_page = args_dict.get('per_page', constants.HOME_PAGE_MAX_NEWS)
    # cid分类
    category_id = args_dict.get('cid', 1)
    # 校验参数
    try:
        page = int(page)
        per_page = int(per_page)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")
    filters = []
    # 查询数据并分页
    if category_id != "1":
        filters.append(News.category_id == category_id)
    try:
        # 加过滤条件的查询
        paginate = News.query.filter(*filters).order_by(News.create_time.desc()).paginate(page, per_page, False)
        # 获取查询的数据,返回当前页的所有数据
        items = paginate.items
        # h获取总页数
        total_page = paginate.pages
        # 当前页数
        current_page = paginate.page
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据查询失败")

    news_li = []

    for news in items:
        news_li.append(news.to_basic_dict())

    return jsonify(errno=RET.OK, errmsg="OK",
                   # 总页数
                   totalPage=total_page,
                   # 当前页
                   currentPage=current_page,
                   # 当前页的新闻数据
                   newsList=news_li,
                   # 分类id
                   cid=category_id)
    # 返回数据


@index_blu.route('/favicon.ico')
def get_web_logo():
    return current_app.send_static_file('news/favicon.ico')
