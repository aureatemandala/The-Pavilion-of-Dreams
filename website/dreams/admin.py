from django.contrib import admin
from dreams.models import Library, Kingdom, Phylum, Article
# Register your models here.

#admin.site.register(Library)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("id","SHUMING")

@admin.register(Kingdom)
class KingdomAdmin(admin.ModelAdmin):
    list_display = ("id", "LEIBIE")

@admin.register(Phylum)
class PhylumAdmin(admin.ModelAdmin):
    list_display = ("id", "LEIBIE", "FATHER")

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "BIAOTI", "CHUANGJIANSHIJIAN")