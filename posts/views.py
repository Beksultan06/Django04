from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from posts.models import Post


def index_view(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


def contacts(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "posts/contacts.html", context)


def about(request):
    context = {
        "title": "О нас"
    }
    return render(request, "posts/about.html", context)

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"] 