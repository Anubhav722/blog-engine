from django.conf.urls import url, include
from blog import views

urlpatterns = [
   url(r'^list/', views.index, name='index'),
   url(r'^(?P<id>\d+)/', views.detail, name='detail'),
]