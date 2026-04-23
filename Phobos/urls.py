"""
Definition of urls for Phobos.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('pool/', views.pool, name='pool'),
    path('registration/', views.registration, name='registration'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:post_id>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('tinymce/', include('tinymce.urls')),
    path('videopost/', views.videopost, name='videopost'),
    path('catalog/', views.catalog, name='catalog'),
    path('category/<int:category_id>', views.category, name='category'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('newcategory/', views.newcategory, name='newcategory'),
    path('newproduct/', views.newproduct, name='newproduct'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
