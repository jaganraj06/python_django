from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,'members/index.html')
def detail(request,post_id ):
    return render(request,'members/detail.html')
def page(request):
    return HttpResponse(" you are viewing page detail page ")
def old_url_redirect(request):
    return redirect(reverse('members:new_page_url'))
def new_url_views(request):
    return HttpResponse("This is the new URL")