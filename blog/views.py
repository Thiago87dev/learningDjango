# from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts
from django.http import Http404



def blog(req):
    contexto = {
    # 'text' : 'Estamos no blog ',
    'title' : 'Blog - ',
    'css': 'global/css/red.css',
    'posts': posts,
    }
    return render(req, 'blog/index.html', contexto)

def post(req, post_id):
    found_post = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
        
    if found_post is None:
        raise Http404('Post não existe')
    
    contexto = {
    # 'text' : 'Estamos no blog ',
    'title' : found_post['title'] + ' - ',
    'css': 'global/css/red.css',
    'post': found_post,
    }
    return render(req, 'blog/post.html', contexto)

def ex(req):
    contexto = {
    'text' : 'Estamos no EX',
    'title':'EX - ',
    'css': 'home/css/blue.css',
    }
    return render(req, 'blog/ex.html', contexto)
