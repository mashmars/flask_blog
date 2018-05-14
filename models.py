from app import db

#用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),unique=True)
    #创建关联 1对多，创建到1的一方 parameter1 对方模型名称 parameter2 对方要用的
    comments = db.relationship('Comment',backref='user')
#评论表
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True)
    article_id = db.Column(db.Integer,db.ForeignKey('article.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    content = db.Column(db.Text)

#分类表
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),unique=True)
#标签表
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),unique=True)
#标签和文章属于多对多 需要中间表
article_tag = db.Table(
    'article_tags',
    db.Column('article_id',db.Integer,db.ForeignKey('article.id')),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'))
)

#文章表
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    tag_id = db.Column(db.Integer,db.ForeignKey('tag.id'))
    createdate = db.Column(db.DateTime)
    content = db.Column(db.Text)
    # 1对多关联
    category = db.relationship('Category',backref='articles')
    #对多对关联
    tags = db.relationship(
        'Tag',
        secondary = article_tag,
        backref = db.backref('articles',lazy='dynamic')
    )

