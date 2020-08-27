from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

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

class Kingdom(models.Model):
    LEIBIE = models.CharField(null=False, blank=True, max_length=50, verbose_name="分类")
    BIEMING = models.CharField(null=False, blank=True, max_length=50, verbose_name="别名")

    def __str__(self):
        return self.LEIBIE
    
class Phylum(models.Model):
    LEIBIE = models.CharField(null=False, blank=True, max_length=50, verbose_name="分类")
    BIEMING = models.CharField(null=False, blank=True, max_length=50, verbose_name="别名")
    FATHER = models.ForeignKey(Kingdom, on_delete=models.DO_NOTHING, verbose_name="父类别")

    def __str__(self):
        return self.LEIBIE


class Article(models.Model):
    BIAOTI = models.CharField(null=False, blank=True, max_length=300, verbose_name="标题")
    ZHENGWEN = RichTextUploadingField(verbose_name="正文")
    ZUOZHE = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者")
    CHUANGJIANSHIJIAN = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    ZUIHOUSHIJIAN = models.DateTimeField(auto_now=True, verbose_name="最后编辑时间")
    DAFENLEI = models.ForeignKey(Kingdom, on_delete=models.DO_NOTHING, verbose_name="大分类")
    XIAOFENLEI = models.ForeignKey(Phylum, on_delete=models.DO_NOTHING, verbose_name="小分类")
    BIAOQIAN = models.CharField(null=False, blank=True, max_length=500, verbose_name="标签")

    def __str__(self):
        return self.BIAOTI