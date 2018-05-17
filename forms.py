from flask_wtf import FlaskForm

from wtforms import StringField,SubmitField,TextAreaField,SelectField,RadioField,SelectMultipleField,widgets
from wtforms.validators import data_required,length

from models import Tag,Category

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=True)
    option_widget = widgets.CheckboxInput()

#tag后台
class TagForm(FlaskForm):
    title = StringField('标题：',validators=[data_required(message='标题不能为空'),length(min=1,message=('长度不能小于1个字符'))])
    submit = SubmitField('立即提交')

#后台文章表单
class ArticleForm(FlaskForm):
    title = StringField('标题',validators=[data_required(message='标题不能为空')])
    descript = TextAreaField('描述')
    category = SelectField('分类',validators=[data_required(message='请选择分类')],choices=[],coerce=int)
    #tag = MultiCheckboxField('标签',validators=[data_required(message='请选择分类')],choices=[],coerce=int)
    content = TextAreaField('内容')
    submit = SubmitField('保存')
    def __init__(self):
        super().__init__()
        category_data = Category.query.all()
        self.category.choices = [(cate.id,cate.title) for cate in category_data]
        #self.category.default= 2

        #tag_data = Tag.query.all()
        #self.tag.choices = [(item.id,item.title) for item in Tag.query.all()] #模板调用{{ form.tag() }} ，样式输出格式问题





