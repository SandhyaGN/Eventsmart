from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('create',views.create,name="create"),
    path('index',views.index,name="index"),
    path('base',views.base,name="base"),
    path('liked',views.liked,name="liked"),
    path('likedevent',views.likedevent,name="likedevent"),
]