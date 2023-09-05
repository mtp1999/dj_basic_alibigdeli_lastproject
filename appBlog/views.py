from django.shortcuts import render, redirect
from django.urls import reverse

from appBlog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from appBlog.forms import ContactForm, CommentForm
from django.contrib import messages


def home_view(request):
    return render(request, 'appBlog/index.html')


def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')

    if s := request.GET.get('search'):
        posts = posts.filter(title__contains=s)
    if a := kwargs.get('author'):
        posts = posts.filter(author__username=a)
    if c := kwargs.get('category'):
        posts = posts.filter(categories__name=c)
    if t := kwargs.get('tag'):
        posts = posts.filter(tags__name__icontains=t)

    posts = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = posts.page(page_number)
    except PageNotAnInteger:
        return redirect('appBlog:post_list')
    except EmptyPage:
        return redirect('appBlog:post_list')

    context = {'posts': posts}
    return render(request, 'appBlog/blog.html', context)


def single_post_view(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment Saved.')
        else:
            messages.error(request, form.errors)
        return redirect('appBlog:single', pid=pid)

    form = CommentForm()
    post_id_list = [post.id for post in Post.objects.all().filter(status=1).order_by('id')]
    post = Post.objects.get(id=pid)
    comments = Comment.objects.filter(post=post, allowed=True)
    try:
        next_post = Post.objects.get(id=post_id_list[post_id_list.index(pid)+1])
    except:
        next_post = None
    try:
        if post_id_list.index(pid) - 1 == -1:
            raise ValueError
        previous_post = Post.objects.get(id=post_id_list[post_id_list.index(pid) - 1])
    except:
        previous_post = None
    try:
        post.views += 1
        post.save()
    except:
        return redirect('appBlog:home')
    context = {
        'form': form,
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'comments': comments
    }
    return render(request, 'appBlog/blog-single.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'message saved.')
            return redirect('appBlog:home')
        else:
            messages.error(request, form.errors)
            return redirect('appBlog:contact')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'appBlog/contact.html', context)


def about_view(request):
    return render(request, 'appBlog/about.html')