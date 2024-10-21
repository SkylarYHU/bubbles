from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

# RegisterForm 继承自 Django 的 UserCreationForm，这意味着它将拥有创建用户所需的默认字段和验证逻辑
class RegisterForm(UserCreationForm):
  # 添加了一个名为 email 的字段，使用 forms.EmailField 定义，确保用户输入的内容是有效的电子邮件地址
  email = forms.EmailField(required=True)

  # 通过 model 属性指定与之关联的 Django 模型（在这里是 User）。这告诉 Django 此表单是为哪个模型设计的，并允许表单使用该模型的字段和验证逻辑。
  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ["title", "description"]