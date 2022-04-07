'''定义URL模式'''
from django.urls import path,include
from . import views

app_name='star14'
urlpatterns=[
    #主页
    path('',views.index,name='index'),
    # display all the topics
    path('topics/',views.topics,name='topics')
]