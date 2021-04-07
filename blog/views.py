from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, resolve
from .models import Post
from .forms import CommentForm

def get_absolute_url(self):
    return "/post/%i/" % self.id

def index(request):
    newest_posts = Post.objects.order_by('-date')
    template = loader.get_template('blog/index.html')
    context = {'newest_posts': newest_posts}
    return HttpResponse(template.render(context, request))


def detail(request, post_id):
    try:
        p = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Error")
    return render(request, 'blog/detail.html', {'post': p})

def comments(request, post_id):
    try:
        p = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Error")
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = p
            comment.save()
            red = get_absolute_url(p)
            return redirect(red)
    else:
        form = CommentForm()
    return render(request, 'blog/comments.html', {'form': form})
