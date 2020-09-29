"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dreams.views import index, shudan, book, music, painting, film, ACG, dreams, author, book_review, classical_music, jazz, rock, spirit, the_bealtes, painter, paintings, filmmaker, film_review, animation, comic, game, note, travels, icarus
from django.conf import settings
from django.conf.urls.static import static 
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('shudan/', shudan, name='shudan'),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path("favicon.ico",RedirectView.as_view(url='media/favicon.ico')),
    path('article/', include('dreams.urls')),
    path('book/', book, name="book"),
    path('music/', music, name="music"),
    path('painting/', painting, name="painting"),
    path('film/', film, name="film"),
    path('ACG/', ACG, name="ACG"),
    path('dreams/', dreams, name="dreams"),
    path('author/', author, name="author"),
    path('book_review/', book_review, name="book_review"),
    path('classical_music/', classical_music, name="classical_music"),
    path('jazz/', jazz, name="jazz"),
    path('rock/', rock, name="rock"),
    path('spirit/', spirit, name="spirit"),
    path('the_bealtes/', the_bealtes, name="the_bealtes"),
    path('painter/', painter, name="painter"),
    path('paintings/', paintings, name="paintings"),
    path('filmmaker/', filmmaker, name="filmmaker"),
    path('film_review/', film_review, name="film_review"),
    path('animation/', animation, name="animation"),
    path('comic/', comic, name="comic"),
    path('game/', game, name="game"),
    path('note/', note, name="note"),
    path('travels/', travels, name="travels"),
    path('icarus/', icarus, name="icarus"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)