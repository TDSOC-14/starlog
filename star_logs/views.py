from django.shortcuts import render

def index(request):
    '''笔记的主页'''
    return render(request,'star_logs/index.html')