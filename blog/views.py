from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    allpost = Blogpost.objects.all()
    params = {
        'allpost':allpost
    }
    return render(request,'blog/index.html',params)

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id = id)[0]
    allpost = Blogpost.objects.all()
    params = {
        'post':post,'allpost':allpost
    }
    return render(request,'blog/blogpost.html',params)

