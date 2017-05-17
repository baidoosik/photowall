from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    post_list =Post.objects.filter(category='은지').all()
    return render(request,'photobook/home.html',{
        'post_list': post_list
    })

def global_challenge(request):
    post_list =Post.objects.filter(category='글로벌 챌린지').all()
    return render(request,'photobook/home.html',{
        'post_list': post_list
    })

def indonesia(request):
    post_list =Post.objects.filter(category='인도네시아 코이카 탐방').all()
    return render(request,'photobook/home.html',{
        'post_list': post_list
    })

def mwc(request):
    post_list =Post.objects.filter(category='바르셀로나mwc').all()
    return render(request,'photobook/home.html',{
        'post_list': post_list
    })