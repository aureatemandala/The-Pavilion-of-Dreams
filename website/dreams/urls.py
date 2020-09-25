from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:article_id>', views.article, name="article"),
]