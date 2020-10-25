from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, Template
from dreams.models import Library, Article, Oracle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random


# Create your views here.
def index(request):
    context = {}

    article_list = Article.objects.all().order_by('-id')

    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')
    
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    context['article_list'] = article_list


    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)
    index_page = render(request,'index.html',context)

    return index_page




def shudan(request):

    context = {}
    book_list = Library.objects.all()
    page_robot = Paginator(book_list, 10)
    page_num = request.GET.get('page')
    
    try:
        book_list = page_robot.page(page_num)
    except EmptyPage:
        book_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        book_list = page_robot.page(1)

    context['book_list'] = book_list

    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'shudan.html',context)

    return index_page



def article(request, article_id):
    context = {}

    article = get_object_or_404(Article, id=article_id)
    context['article'] = article
    context[ 'previous_article' ] = Article.objects.filter(id__lt=article.id).last()
    context[ 'next_article' ] = Article.objects.filter(id__gt=article.id).first()

    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request, 'article.html', context)
    return index_page


def book(request):
    context = {}

    article_list = Article.objects.filter(DAFENLEI="1").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def music(request):
    context = {}

    article_list = Article.objects.filter(DAFENLEI="2").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page


    
def painting(request):
    context = {}

    article_list = Article.objects.filter(DAFENLEI="3").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page


    
def film(request):
    context = {}

    article_list = Article.objects.filter(DAFENLEI="4").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page


    
def ACG(request):
    context = {}

    article_list = Article.objects.filter(DAFENLEI="5").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page


    
def dreams(request):
    context = {}

    article_list = Article.objects.filter(DAFENLEI="6").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page


def author(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="1").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def book_review(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="2").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def classical_music(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="3").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def jazz(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="4").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def rock(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="5").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def spirit(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="6").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def the_bealtes(request):
    context = {}

    # article_list = Article.objects.filter(XIAOFENLEI="7").order_by('-id')
    # page_robot = Paginator(article_list, 10)
    # page_num = request.GET.get('page')

    # try:
    #     article_list = page_robot.page(page_num)
    # except EmptyPage:
    #     article_list = page_robot.page(page_robot.num_pages)
    # except PageNotAnInteger:
    #     article_list = page_robot.page(1)
    
    # context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'thebeatleslrc.html',context)
    return index_page

def painter(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="8").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def paintings(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="9").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def filmmaker(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="10").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def film_review(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="11").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def animation(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="12").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def comic(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="13").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def game(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="14").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def note(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="15").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def travels(request):
    context = {}

    article_list = Article.objects.filter(XIAOFENLEI="16").order_by('-id')
    page_robot = Paginator(article_list, 10)
    page_num = request.GET.get('page')

    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    
    context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'index.html',context)
    return index_page

def icarus(request):
    context = {}

    # article_list = Article.objects.filter(XIAOFENLEI="17").order_by('-id')
    # page_robot = Paginator(article_list, 10)
    # page_num = request.GET.get('page')

    # try:
    #     article_list = page_robot.page(page_num)
    # except EmptyPage:
    #     article_list = page_robot.page(page_robot.num_pages)
    # except PageNotAnInteger:
    #     article_list = page_robot.page(1)
    
    # context['article_list'] = article_list
    
    oracle_list = Oracle.objects.all()
    context['oracle'] = random.choice(oracle_list)

    index_page = render(request,'icarus.html',context)
    return index_page
