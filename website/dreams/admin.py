from django.contrib import admin
from dreams.models import Library, Kingdom, Phylum, Article, Oracle
# Register your models here.

#admin.site.register(Library)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("id","SHUMING")

@admin.register(Kingdom)
class KingdomAdmin(admin.ModelAdmin):
    list_display = ("id", "LEIBIE", "BIEMING")

@admin.register(Phylum)
class PhylumAdmin(admin.ModelAdmin):
    list_display = ("id", "LEIBIE", "BIEMING", "FATHER")

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("BIAOTI", "id", "CHUANGJIANSHIJIAN", "DAFENLEI", "XIAOFENLEI")


@admin.register(Oracle)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("ZUOZHE", "id", "ZHENGWEN")

