from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from blogapp.models import Post

# Create your views here.

def all_posts(request:HttpRequest):
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


@csrf_exempt
def create_post(request:HttpRequest):
    if(request.method == 'POST'):
        print("POST request handled")
        title = request.POST.get('title')
        content = request.POST.get('content')
        print('title = ', title)
        print('content = ', content)
        new_post = Post(title = title, content=content)
        new_post.save()
    return render(request, "blogapp/post-form.html")