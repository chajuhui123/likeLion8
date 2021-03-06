from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at=models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #ForeignKey는 외래키. 모델과 연결하려면 첫 번째 인자는 모델이름, 두 번째 인자는 옵션
    #on_delete = models.CASCADE 위의 모델이 지워지면 종속되어있는 모델도 같이 지워진다!
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content #admind에서 모델을 content로 보이게 하고 싶어서
        
