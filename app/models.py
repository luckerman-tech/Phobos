from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = 'posted', verbose_name = 'Заголовок')
    description = models.CharField(max_length = 1000, blank = True, verbose_name = 'Краткое содержание')
    image = models.ImageField(null = True, blank = True, verbose_name = 'Фотография')
    content = models.TextField(verbose_name = 'Полное содержание')
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = 'Дата и время публикации')
    author = models.ForeignKey(User, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = 'Автор')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost', args=[str(self.id)])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-posted']
        db_table = 'News'

class Comment(models.Model):
    text = models.CharField(max_length = 1000, verbose_name = 'Текст комментария')
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = 'Дата и время оставления комментария')
    author = models.ForeignKey(User, null = True, on_delete = models.SET_NULL, verbose_name = 'Автор комментария')
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = 'Новость, к которой относится комментарий')

    def __str__(self):
        return f'Комментарий №{self.id}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date']
        db_table = 'Comments'

class Category(models.Model):
    title = models.CharField(max_length = 100, unique = True, db_index = True, verbose_name = 'Название')
    desc = models.TextField(blank = True, verbose_name = 'Описание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])

    class Meta:
        verbose_name = 'Категория каталога'
        verbose_name_plural = 'Категории каталога'
        ordering = ['title']
        db_table = 'Categories'

class Product(models.Model):
    title = models.CharField(max_length = 100, unique = True, db_index = True, verbose_name = 'Название')
    short_desc = models.CharField(max_length = 1000, blank = True, verbose_name = 'Краткое описание')
    full_desc = models.TextField(verbose_name = 'Полное описание')
    price = models.DecimalField(max_digits = 10, decimal_places = 2, validators = [MinValueValidator(0.01, 'Цена должна быть положительным числом')], verbose_name = 'Цена')
    image = models.ImageField(verbose_name = 'Изображение')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])

    class Meta:
        verbose_name = 'Элемент каталога'
        verbose_name_plural = 'Элементы каталога'
        ordering = ['title']
        db_table = 'Products'

admin.site.register(Comment)
