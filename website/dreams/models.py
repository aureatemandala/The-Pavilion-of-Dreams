from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    article_body = models.TextField(null=True)
    author = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.title