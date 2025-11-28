from django.http import HttpResponse
from .models import BlogPost
from django.shortcuts import render, get_object_or_404

#Mithul part
def home(request):
    data = BlogPost.objects.all()
    return render(request, "home.html", {"post": data})

#Kishore Part
def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'post_detail.html',{'post':post})

def create(request):
    return HttpResponse("Create a new post")

def edit_post(request, id):
    return HttpResponse("Edit an existing post")

def delete_post(request, id):
    return HttpResponse("Delete an existing post")
