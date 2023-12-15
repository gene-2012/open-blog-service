from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blogs.models import Blog
from .forms import PageForm
#from markdown2 import markdown
from django.http import HttpResponseForbidden
# Create your views here.
def user_home(request, user_id):
    """
    .TODO : add markdown viewer
    """
    user = get_object_or_404(get_user_model(), id=user_id)
    context = {'page_user' : user, 'profile' : user.page}
    return render(request, 'user/user.html', context)
def user_blog(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    context = {'page_user' : user, 'blogs' : Blog.objects.filter(Q(owner = user))}
    return render(request, 'user/user_blog.html', context)
def user(request, user_id, page_id):
    if page_id == 'home':
        return user_home(request, user_id)
    elif page_id == 'blogs':
        return user_blog(request, user_id)
@login_required
def my(request, page_id):
    return user(request, request.user.id, page_id)
    
@login_required
def my_home(request):
    return user_home(request, request.user.id)
@login_required
def edit_page(request, id):
    user = get_user_model().objects.get(id=id)
    permission = request.user.is_superuser or request.user == user
    if not permission:
        return HttpResponseForbidden()
    if request.method != 'POST':
        form = PageForm(instance=user)
    else:
        form = PageForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/user/{id}/home')
    context = {'page': user, 'form' : form}
    return render(request, 'user/edit_page.html', context)
