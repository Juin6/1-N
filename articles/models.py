from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # comment_set 라는 컬럼도 foreignkey에 의해 자동으로 생성됨.

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id 라는 컬럼은 자동으로 생성해줌