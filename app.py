from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
import config
import datetime
from models import *

app = Flask(__name__)
#加载配置
app.config.from_object(config)

db = SQLAlchemy()
db.init_app(app)

@app.route('/')
def home():
    return '首页'
#添加数据
@app.route('/add')
def add():
    article = Article()
    article.title = '文章标题4'
    article.content = '哈哈，blog正在进行中4...'
    article.createdate = datetime.datetime.now()
    cate = Category.query.get(1)
    # tag = Tag.query.filter(Tag.id > 1).all()
    tag = db.session.query(Tag).filter(Tag.id > 1).all()
    article.category_id = cate.id
    # article.tag_id = tag.id#完全没必要有这一列
    article.tags = tag #多对多用
    #article.tags = [tag] #1对多用
    db.session.add(article)
    db.session.commit()
    return 'success';



if __name__ == '__main__':
    app.run()