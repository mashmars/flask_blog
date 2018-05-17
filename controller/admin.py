from flask import Blueprint,render_template,request,url_for,redirect,flash,jsonify
from forms import TagForm,ArticleForm
from models import db,Tag,Category,Article

import datetime
admin_bp = Blueprint('admin',__name__,url_prefix='/admin')

#后台主页
@admin_bp.route('/index/')
def admin_index():
    return render_template('admin/index.html')
#标签
@admin_bp.route('/tag/')
def tag():
    tags = Tag.query.order_by(Tag.id.desc()).all()
    return render_template('admin/tag.html',tags=tags)
#标签添加页面
@admin_bp.route('/tag/add/',methods=['GET','POST'])
def tag_add():
    form = TagForm()
    if form.is_submitted() and form.validate_on_submit():
        tag = Tag()
        tag.title = form.title.data
        db.session.add(tag)
        db.session.commit()
        return redirect(url_for('admin.tag'))
    return render_template('admin/tag_add.html',form=form)
#标签编辑页面
@admin_bp.route('/admin/tag/<int:id>/edit/',methods=['GET','POST'])
def tag_edit(id):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    if form.is_submitted() and form.validate_on_submit():
        tag.title = form.title.data
        db.session.commit()
        return redirect(url_for('admin.tag'))
    return render_template('admin/tag_edit.html',form=form,tag=tag)
#标签删除页面
@admin_bp.route('/admin/tag/<int:id>/delete/')
def tag_del(id):
    tag = Tag.query.get_or_404(id)
    db.session.delete(tag)
    db.session.commit()
    flash('删除成功')
    return redirect(url_for('admin.tag'))

#分类列表页
@admin_bp.route('/category/')
def category():
    categorys = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/category.html',categorys=categorys)
#分类添加页
@admin_bp.route('/category/add/',methods=['GET','POST'])
def category_add():
    form = TagForm()
    if form.is_submitted() and form.validate_on_submit():
        category = Category()
        category.title = form.title.data
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('admin.category'))
    return render_template('admin/category_add.html',form=form)
#分类编辑页
@admin_bp.route('/category/<int:id>/edit/',methods=['GET','POST'])
def category_edit(id):
    category = Category.query.get_or_404(id)
    form = TagForm()
    if form.is_submitted() and form.validate_on_submit():
        category.title = form.title.data
        db.session.commit()
        return redirect(url_for('admin.category'))
    return render_template('admin/category_edit.html',category=category,form=form)
#分类删除
@admin_bp.route('/category/<int:id>/delete')
def category_del(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('admin.category'))
#文章列表
@admin_bp.route('/article/')
def article():
    page = request.args.get('page',1)
    d = Article.query.order_by(Article.id.desc()).paginate(int(page),5)
    #print(d.items)
    return render_template('admin/article.html',article=d)
#文章添加页面
@admin_bp.route('/article/add/',methods=['GET','POST'])
def article_add():
    form = ArticleForm()
    if form.is_submitted() and form.validate_on_submit():
        article = Article();
        article.title = form.title.data
        article.descript = form.descript.data
        article.content = form.content.data
        article.category_id = form.category.data
        #tags = Tag.query.filter(Tag.id.in_(form.tag.data)).all() #forms.py
        tags = Tag.query.filter(Tag.id.in_(request.form.getlist('tag_zidingyi'))).all()
        article.tags = tags
        article.createdate = datetime.datetime.now()
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('admin.article'))
    tags = Tag.query.all()

    return render_template('admin/article_add.html',form=form,tags=tags)
#文章编辑也
@admin_bp.route('/article/<int:id>/edit/',methods=['GET','POST'])
def article_edit(id):
    article = Article.query.get_or_404(id)
    #form = ArticleForm()
    #form.title.default =article.title
    #form.category.default =article.category_id
    #form.descript.default = article.descript
    #form.content.default = article.content
   # form.process() #更改默认 必须执行这个 但是csrf提示The CSRF token is missing
    #if form.is_submitted() and form.validate_on_submit():
        #article.title = form.title.data
        #article.category_id = form.category.data
        #article.descript = form.descript.data
        #article.content = form.content.data
        #article.tags = Tag.query.filter(Tag.id.in_(request.form.getlist('tag_zidingyi'))).all()
        #db.session.commit()
        #return redirect(url_for('admin.article'))
    if request.method == 'POST':
        article.category_id = request.form.get('category')
        article.title = request.form.get('title')
        article.descript = request.form.get('descript')
        article.content = request.form.get('content')
        article.tags = Tag.query.filter(Tag.id.in_(request.form.getlist('tag_zidingyi'))).all()
        db.session.commit()
        return redirect(url_for('admin.article'))

    tags = Tag.query.all()
    categorys = Category.query.all()
    return render_template('admin/article_edit.html',article=article,tags=tags,categorys=categorys)
#文章删除 ajax
@admin_bp.route('/article/delete/',methods=['POST'])
def article_del():
    id = request.values.get('id')
    article = Article.query.get(id)
    if not article:
        return jsonify({'code':404,'msg':'请求有误'})
    db.session.delete(article)
    db.session.commit()
    return jsonify({'code':0,'msg':'删除成功'})