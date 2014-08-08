
from django.core.urlresolvers import reverse
from django.template import RequestContext
# Views to be created
# display your categories and latest posts
# display your posts in a specific category
# display the posts

# Create your views here.
from blog.models import Blog, Category
from blog.forms import PostForm, CategoryForm
from django.shortcuts import render_to_response, get_object_or_404, redirect, render

def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('blog/view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
def post_new(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('post_edit')
    return render_to_response('blog/post_edit.html', {'form': form}, RequestContext(request))

def category_new(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_edit')
        else:
            return redirect('category_edit')
    return render_to_response('blog/category_edit.html', {'form': form}, RequestContext(request))
    