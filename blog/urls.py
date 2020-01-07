from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'), # if there is nothing after blog/ call the views.py allblogs
    path('<int:blog_id>/', views.detail, name='detail'), # look for an int after /blog and we'll save it as blog_id
]