from django.http import HttpResponse
from django.shortcuts import render

from blogapp.models import Post

# Create your views here.

def all_posts(request):
    context = {
        'posts':Post.objects.all()
    }

    return render(request,'blogapp/index.html',context=context)


def post_by_id(request, id):
    
    context = {
        'id': id,
        'post' : Post.objects.get(id=id)
    }
    return render(request,'blogapp/post.html', context=context)