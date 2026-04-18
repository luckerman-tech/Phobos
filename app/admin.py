from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from app.models import Blog
import re

class BlogAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = TinyMCE()
        return super().formfield_for_dbfield(db_field, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        original_clean = getattr(form, 'clean_content', None)
        
        def clean_content(self):
            content = self.cleaned_data['content']
            content = content.replace('<br>', ' ').replace('<br/>', ' ').replace('<br />', ' ')
            content = re.sub(r'\s+', ' ', content)
            return content
        
        form.clean_content = clean_content
        return form

admin.site.register(Blog, BlogAdmin)
