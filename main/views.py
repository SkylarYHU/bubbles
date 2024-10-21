from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
@login_required(login_url="/login")
def home(request):
  posts = Post.objects.all()
  if request.method == "POST":
    post_id = request.POST.get("post-id")
    post = Post.objects.filter(id=post_id).first()
    if post and post.author == request.user:
      post.delete()
  return render(request, "main/home.html", {"posts":posts})

@login_required(login_url="/login")
def create_post(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit = False)
      post.author = request.user
      post.save()
      return redirect("/home")
  else:
    form = PostForm()

  return render(request, "main/create_post.html", {"form": form})

def sign_up(request):
  # 如果请求是 POST，使用 RegisterForm 来实例化一个表单对象，并将提交的表单数据（request.POST）传递给它。
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/home')
  else:
    # 如果请求不是 POST（例如 GET 请求），则创建一个空的 RegisterForm 实例
    form = RegisterForm()

  return render(request, "registration/sign_up.html", {"form": form})
