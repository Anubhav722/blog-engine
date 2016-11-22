from django.contrib import admin

# Register your models here.
from blog.models import Content, Content_Types

admin.site.register(Content)
admin.site.register(Content_Types)