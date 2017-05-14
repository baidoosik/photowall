from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    post_list =Post.objects.filter(category='미국').all()
    return render(request,'photobook/home.html',{
        'post_list': post_list
    })

def lover(request):
    post_list =Post.objects.filter(category='은지').all()
    return render(request,'photobook/home.html',{
        'post_list': post_list
    })