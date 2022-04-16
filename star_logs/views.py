from django.shortcuts import render
from django.shortcuts import render
from .models import Topic

def index(request):
    '''笔记的主页'''
    return render(request,'star_logs/index.html')

def topics(request):
    '''display all the topics in the page'''
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(request,'star_logs/topics.html',context)
def topic(request,topic_id):
    '''显示单个主题及所有的条目'''
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'star_logs/topic.html',context)