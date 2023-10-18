from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from blogapp.forms import PostForm

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
    form = PostForm()
    if(request.method == 'POST'):
        form = PostForm(data=request.POST)
        form.save()
        return redirect('posts')

    context = {'form':form,}
    return render(request, "blogapp/post-form.html", context)