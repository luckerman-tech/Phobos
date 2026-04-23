"""
Definition of views.
"""

from app.forms import PoolForm, CommentForm, BlogForm, CategoryForm, ProductForm
from app.models import Blog, Comment, Category, Product
from datetime import datetime
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    latest_news = Blog.objects.all()[:3]
    return render(
        request,
        'app/index.html',
        {
            'title': 'Главная',
            'year': datetime.now().year,
            'latest_news': latest_news,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Наши контакты',
            'year': datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'О сайте',
            'year': datetime.now().year,
        }
    )

def links(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title': 'Полезные ресурсы',
            'year': datetime.now().year,
        }
    )

def pool(request):
    assert isinstance(request, HttpRequest)
    data = dict()
    labels = dict()
    if request.method == 'POST':
        form = PoolForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for field in form.fields:
                labels[field] = form.fields[field].label
            form = None
    else:
        form = PoolForm()
    return render(
        request,
        'app/pool.html',
        {
            'title': 'Обратная связь',
            'year': datetime.now().year,
            'form': form,
            'data': data,
            'labels': labels,
        }
    )

def registration(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            login(request, reg_f)
            return redirect('home')
    else:
        regform = UserCreationForm()
    return render(
        request,
        'app/registration.html',
        {
            'title': 'Регистрация',
            'year': datetime.now().year,
            'regform': regform,
        }
    )

def blog(request):
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all()
    return render(
        request,
        'app/blog.html',
        {
            'title': 'Новости',
            'posts': posts,
            'year': datetime.now().year,
        }
    )

def blogpost(request, post_id):
    assert isinstance(request, HttpRequest)
    post = Blog.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit = False)
            comment_f.date = datetime.now()
            comment_f.author = request.user
            comment_f.post = post
            comment_f.save()
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm()
    return render(
        request,
        'app/blogpost.html',
        {
            'title': 'Новость',
            'post': post,
            'year': datetime.now().year,
            'comments': comments,
            'form': form,
        }
    )

def newpost(request):
    assert isinstance(request, HttpRequest)
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_f = form.save(commit = False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(
        request,
        'app/newpost.html',
        {
            'title': 'Добавить новость',
            'year': datetime.now().year,
            'form': form,
        }
    )

def videopost(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title': 'Полезные видео',
            'year': datetime.now().year,
        }
    )

def catalog(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    return render(
        request,
        'app/catalog.html',
        {
            'title': 'Каталог товаров и услуг',
            'year': datetime.now().year,
            'categories': categories,
        }
    )

def category(request, category_id):
    assert isinstance(request, HttpRequest)
    cur_category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=cur_category)
    return render(
        request,
        'app/category.html',
        {
            'title': 'Категория',
            'year': datetime.now().year,
            'category': cur_category,
            'products': products,
        }
    )

def product(request, product_id):
    assert isinstance(request, HttpRequest)
    cur_product = Product.objects.get(id=product_id)
    return render(
        request,
        'app/product.html',
        {
            'title': 'Продукт',
            'year': datetime.now().year,
            'product': cur_product,
        }
    )

def newcategory(request):
    assert isinstance(request, HttpRequest)
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = CategoryForm()
    return render(
        request,
        'app/newcategory.html',
        {
            'title': 'Добавить категорию каталога',
            'year': datetime.now().year,
            'form': form,
        }
    )

def newproduct(request):
    assert isinstance(request, HttpRequest)
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()
    return render(
        request,
        'app/newproduct.html',
        {
            'title': 'Добавить элемент каталога',
            'year': datetime.now().year,
            'form': form,
        }
    )
