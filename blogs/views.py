from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from markdown2 import markdown
from django.utils.safestring import mark_safe
# Create your views here.

def index(request):
    limit = 50
    blogs = Blog.objects.order_by('-date_added').values_list('id', flat=True)[:limit]
    blogs = Blog.objects.filter(id__in=blogs).order_by('-date_added')
    
    for blog in blogs:
        blog.text = blog.__str__()

    context = {'blogs' : blogs}
    return render(request, 'blogs/index.html', context)

def blogs(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
               'blog' : blog, 
               'title' : blog.title, 
               'owner' : blog.owner, 
               'date_added' : blog.date_added, 
               'text' : mark_safe(markdown(blog.text)), 
               'topic' : blog.topic
               }
    return render(request, 'blogs/blogs.html', context)
@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            selected_topic = form.cleaned_data['topics']
            new_blog = form.save(commit=False)
            new_blog.topic = selected_topic
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:index')
    
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)
@login_required
def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    topic = blog.topic
    user = blog.owner
    permission = request.user.is_superuser or request.user == user
    if not permission:
        return HttpResponseForbidden()
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        # POST data submitted; process data.
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    
    context = {'blog': blog, 'topic': topic, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)

@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    user = blog.owner
    permission = request.user.is_superuser or request.user == user
    if not permission:
        return HttpResponseForbidden()
    blog.delete()
    return redirect('blogs:index')