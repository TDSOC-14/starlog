from django.db import models

class Topic(models.Model):
    '''
    笔记主题
    '''
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''返回字符串'''
        return self.text
        
class Entry(models.Model):
    '''帖子或通知主题'''
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='entries'
    def __str__(self):
        return f'{self.text[:50]}'
