"""
Definition of forms.
"""

from app.models import Blog, Comment
from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE
import re

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    name = forms.CharField(label='Ваше имя (или псевдоним):', min_length=2, max_length=50,
                           widget=forms.TextInput({
                               'class': 'form-control',
                               'pattern': '^\\S.*\\S$|^\\S$',
                               'placeholder': 'Текст не должен начинаться и заканчиваться пробелами'}))
    email = forms.EmailField(label='Электронная почта:', min_length=7, max_length=70,
                             widget=forms.EmailInput({
                                 'class': 'form-control'}))
    age = forms.IntegerField(required=False, label='Ваш возраст:', min_value=14, max_value=120,
                             widget=forms.NumberInput({
                                 'class': 'form-control'}))
    city = forms.CharField(required=False, label='Город проживания:', min_length=2, max_length=50,
                           widget=forms.TextInput({
                               'class': 'form-control',
                               'pattern': '^\\S.*\\S$|^\\S$',
                               'placeholder': 'Текст не должен начинаться и заканчиваться пробелами'}))
    frequency_of_visits = forms.ChoiceField(label='Как часто вы заходите на «Фобос»?', 
                                            choices=(('Впервые здесь', 'Впервые здесь'), ('Несколько раз в месяц', 'Несколько раз в месяц'),
                                                     ('Примерно раз в неделю', 'Примерно раз в неделю'), ('Несколько раз в неделю', 'Несколько раз в неделю'),
                                                     ('Практически ежедневно', 'Практически ежедневно')),
                                            widget=forms.RadioSelect({
                                                'class': 'form-check-input'}))
    purpose_of_visit = forms.ChoiceField(label='С какой целью вы чаще всего заходите на сайт?', 
                                         choices=(('Хочу узнать название своего страха', 'Хочу узнать название своего страха'), 
                                                  ('Читаю про конкретную фобию', 'Читаю про конкретную фобию'),
                                                  ('Прохожу тесты', 'Прохожу тесты'), ('Ищу поддержку/истории других', 'Ищу поддержку/истории других'),
                                                  ('Просто интересно', 'Просто интересно'), ('Другое', 'Другое')),
                                         widget=forms.RadioSelect({
                                             'class': 'form-check-input'}))
    visited_sections = forms.MultipleChoiceField(required=False, label='Какие разделы сайта вы посещали?',
                                                 choices=(('Каталог фобий', 'Каталог фобий'), ('Карта страхов', 'Карта страхов (интерактивная)'),
                                                          ('Тесты и опросники', 'Тесты и опросники'), ('Звуки страха', 'Звуки страха'),
                                                          ('Истории сообщества', 'Истории сообщества'), ('Статьи и исследования', 'Статьи и исследования'),
                                                          ('Генератор случайной фобии', 'Генератор случайной фобии')),
                                                 widget=forms.CheckboxSelectMultiple({
                                                     'class': 'form-check-input'}))
    liked = forms.MultipleChoiceField(required=False, label='Что вам понравилось больше всего?',
                                      choices=(('Дизайн и атмосфера', 'Дизайн и атмосфера'), ('Удобство навигации', 'Удобство навигации'),
                                               ('Полнота информации о фобиях', 'Полнота информации о фобиях'), ('Интерактивные элементы', 'Интерактивные элементы (тесты, звуки, карта)'),
                                               ('Истории реальных людей', 'Истории реальных людей'), ('Научная достоверность', 'Научная достоверность'),
                                               ('Скорость работы сайта', 'Скорость работы сайта')),
                                      widget=forms.CheckboxSelectMultiple({
                                          'class': 'form-check-input'}))
    ease_of_search = forms.ChoiceField(label='Оцените удобство поиска фобий по сайту:', 
                                       choices=((1, '1 — Очень неудобно, ничего не нашёл(ла)'), 
                                                (2, '2'), (3, '3'), (4, '4'), 
                                                (5, '5 — Всё интуитивно, нашёл(ла) всё мгновенно')),
                                       widget=forms.RadioSelect({
                                           'class': 'form-check-input'}))
    how_scary = forms.ChoiceField(label='Насколько страшно вам было на сайте?', 
                                  choices=((1, '1 — Совсем не страшно, хотелось зевать'), 
                                           (2, '2'), (3, '3'), (4, '4'), 
                                           (5, '5 — Очень атмосферно, мурашки по коже')),
                                  widget=forms.RadioSelect({
                                      'class': 'form-check-input'}))
    fears_of_animals = forms.ChoiceField(label='Какая фобия из категории «Животные» вас интересует больше всего?',
                                         choices=(('Никакая', 'Никакая фобия не интересует'),
                                                  ('Арахнофобия', 'Арахнофобия (пауки)'), 
                                                  ('Кинофобия', 'Кинофобия (собаки)'), 
                                                  ('Офидиофобия', 'Офидиофобия (змеи)'),
                                                  ('Другое', 'Другое')))
    fears_of_nature = forms.ChoiceField(label='Какая фобия из категории «Природные явления» вас интересует больше всего?',
                                        choices=(('Никакая', 'Никакая фобия не интересует'),
                                                 ('Астрафобия', 'Астрафобия (гроза)'), 
                                                 ('Антофобия', 'Антофобия (цветы)'), 
                                                 ('Никтофобия', 'Никтофобия (темнота)'),
                                                 ('Другое', 'Другое')))
    social_fears = forms.ChoiceField(label='Какая фобия из категории «Социальные фобии» вас интересует больше всего?',
                                     choices=(('Никакая', 'Никакая фобия не интересует'),
                                              ('Социофобия', 'Социофобия'), 
                                              ('Скопофобия', 'Скопофобия (пристальный взгляд)'), 
                                              ('Глоссофобия', 'Глоссофобия (публичные выступления)'),
                                              ('Другое', 'Другое')))
    medical_fears = forms.ChoiceField(label='Какая фобия из категории «Медицинские фобии» вас интересует больше всего?',
                                      choices=(('Никакая', 'Никакая фобия не интересует'),
                                               ('Трипанофобия', 'Трипанофобия (иглы)'), 
                                               ('Дентофобия', 'Дентофобия (стоматологи)'), 
                                               ('Гемофобия', 'Гемофобия (кровь)'),
                                               ('Другое', 'Другое')))
    fears_of_spaces = forms.ChoiceField(label='Какая фобия из категории «Фобии пространств» вас интересует больше всего?',
                                        choices=(('Никакая', 'Никакая фобия не интересует'),
                                                 ('Клаустрофобия', 'Клаустрофобия (узкие пространства)'), 
                                                 ('Агорафобия', 'Агорафобия (толпы людей и большие открытые пространства)'), 
                                                 ('Акрофобия', 'Акрофобия (высота)'),
                                                 ('Другое', 'Другое')))
    strange_and_rare = forms.ChoiceField(label='Какая фобия из категории «Странные и редкие фобии» вас интересует больше всего?',
                                         choices=(('Никакая', 'Никакая фобия не интересует'),
                                                  ('Номофобия', 'Номофобия (страх остаться без телефона)'), 
                                                  ('Папафобия', 'Папафобия (страх Папы Римского)'), 
                                                  ('Гиппопотомонстросескипедалофобия', 'Гиппопотомонстросескипедалофобия (страх длинных слов)'),
                                                  ('Другое', 'Другое')))
    gender = forms.ChoiceField(label='Ваш пол:',
                               choices=(('Неизвестно', 'Не хочу указывать'), 
                                        ('Мужской', 'Мужской'), 
                                        ('Женский', 'Женский')))
    flaws = forms.CharField(required=False, label='Каких фобий или функций вам не хватает на сайте?', 
                            max_length=3000,
                            widget=forms.Textarea({
                                'class': 'form-control',
                                'rows': 6,
                                'placeholder': 'Вводите текст'}))
    wishes = forms.CharField(required=False, label='Что бы вы хотели улучшить или добавить?', 
                             max_length=3000,
                             widget=forms.Textarea({
                                 'class': 'form-control',
                                 'rows': 6,
                                 'placeholder': 'Вводите текст'}))
    share_a_story = forms.CharField(required=False, label='Если хотите поделиться историей своего страха — напишите её здесь!', 
                                    max_length=10000,
                                    widget=forms.Textarea({
                                        'class': 'form-control',
                                        'rows': 12,
                                        'placeholder': 'Вводите текст'}))
    consent_data = forms.BooleanField(label='Я согласен(на) на обработку персональных данных:')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {'text': forms.Textarea({
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Оставьте ваш комментарий...'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = ''

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'image', 'content',)
        widgets = {'title': forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Не более 100 символов'}),
                   'description': forms.Textarea({
            'class': 'form-control',
            'rows': 8,
            'placeholder': 'Не более 1000 символов'}),
                   'image': forms.FileInput({
            'class': 'form-control'}),
                   'content': TinyMCE()}

    def clean_content(self):
        content = self.cleaned_data['content']
        content = content.replace('<br>', ' ').replace('<br/>', ' ').replace('<br />', ' ')
        content = re.sub(r'\s+', ' ', content)
        return content