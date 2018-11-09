from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import post


def post_index(request):
    Xposts = post.objects.all()
    return render(request, 'post/index.html', {'posts': Xposts})


def post_detail(request, id):
    postdetay = get_object_or_404(post, id=id)

    return render(request, 'post/detail.html', {'post': postdetay})


def post_create(request):
    return HttpResponse('Burasi Post Create Sayfası')


def post_update(request):
    return HttpResponse('Burası Post Update Sayfası')


def post_delete(request):
    return HttpResponse('Burası Post Delete Sayfası')
