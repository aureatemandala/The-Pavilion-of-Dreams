from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    index_page = render(request,'index.html',context)

    return index_page

def shudan(request):
    context = {}
    index_page = render(request,'shudan.html',context)

    return index_page