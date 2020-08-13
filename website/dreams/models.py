from django.db import models

# Create your models here.
class Library(models.Model):
    ISBN = models.CharField(null=False, blank=True, max_length=200, verbose_name="ISBN")
    SHUMING = models.CharField(null=True, blank=True, max_length=200, verbose_name="书名")
    ZUOZHE = models.CharField(null=True, blank=True, max_length=200, verbose_name="作者")
    CHUBANSHE = models.CharField(null=True, blank=True, max_length=200, verbose_name="出版社")
    CHUPINFANG = models.CharField(null=True, blank=True, max_length=200, verbose_name="出品方")
    FUBIAOTI = models.CharField(null=True, blank=True, max_length=200, verbose_name="副标题")
    YUANZUOMING = models.CharField(null=True, blank=True, max_length=200, verbose_name="原作名")
    YIZHE = models.CharField(null=True, blank=True, max_length=200, verbose_name="译者")
    CHUBANNIAN = models.CharField(null=True, blank=True, max_length=200, verbose_name="出版年")
    YESHU = models.CharField(null=True, blank=True, max_length=200, verbose_name="页数")
    DINGJIA = models.CharField(null=True, blank=True, max_length=200, verbose_name="定价")
    ZHUANGZHEN = models.CharField(null=True, blank=True, max_length=200, verbose_name="装帧")
    CONGSHU = models.CharField(null=True, blank=True, max_length=200, verbose_name="丛书")
    GUOJI = models.CharField(null=True, blank=True, max_length=200, verbose_name="国籍")
    JIANJIE = models.TextField(null=True, blank=True, verbose_name="简介")
    FENGMIAN = models.CharField(null=True, blank=True, max_length=200, verbose_name="封面")

    def __str__(self):
        return self.SHUMING