from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from dreams.models import Library
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    context = {}
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
    index_page = render(request,'shudan.html',context)

    return index_page