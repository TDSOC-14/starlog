'''定义URL模式'''
from django.urls import path,include
from . import views

app_name='star_logs'
urlpatterns=[
    #主页
    path('',views.index,name='index'),
    # display all the topics
    path('topics/',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #用于添加新主题
    path('new_topic/',views.new_topic,name='new_topic'),
]