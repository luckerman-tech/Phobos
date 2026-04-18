from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = 'posted', verbose_name = 'Заголовок')
    description = models.CharField(max_length = 1000, blank = True, verbose_name = 'Краткое содержание')
    image = models.FileField(null = True, blank = True, verbose_name = 'Фотография')
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

admin.site.register(Comment)
