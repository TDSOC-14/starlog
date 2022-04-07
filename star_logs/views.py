from django.shortcuts import render
from .models import Topic

def index(request):
    '''笔记的主页'''
    return render(request,'star_logs/index.html')
def topics(request):
    '''display all the topics in the page'''
    topics=Topic.objects.order_by('date_added')
    context={'话题':topics}
    return render(request,'star_logs/topics.html',context)