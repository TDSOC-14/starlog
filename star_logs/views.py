from django.shortcuts import render
from django.shortcuts import render
from .models import Topic
from .forms import TopicForm

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

def new_topic(request):
    '''添加新主题'''
    if request.method !='POST':
        #未提交表单：创建
        form=TopicForm()
    else:
        #POST提交的数据：处理
        form=TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request,'star_logs:topics')

    #显示空表单或指出数据无效
    context={'form':form}
    return render(request,'star_logs/new_topic.html',context)