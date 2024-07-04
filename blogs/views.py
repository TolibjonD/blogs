from django.shortcuts import render, redirect
from .models import Blogs
from django.contrib import messages
from .forms import BlogForm
from django.db.models import Q
from django.contrib.auth import logout

def logout(request):
    logout(request)
    return redirect("blogs:index")

def index(request):
    form = BlogForm()
    blogs = Blogs.objects.all().order_by("-created_at")
    q = request.GET.get('q', '')
    count=0
    if q:
        q = request.GET.get('q', '')
        blogs =  blogs = Blogs.objects.filter(Q(title__icontains=q) | Q(blog_text__icontains=q))
        count = blogs.count()
    if request.method == 'POST':
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if request.user.is_authenticated and request.user.is_superuser:
                form.save()
                messages.success(request, "New blog was created successfully ! Thank you for right and useful blog sharing !...")
                return redirect("blogs:index")
            else:
                messages.info(request, "We're sorry only super users can write new blogs !")
                return redirect("blogs:index")
    else:
        delete_id = request.GET.get("delete_id")
        if delete_id :
            if request.user.is_authenticated and request.user.is_superuser:
                blog = Blogs.objects.get(slug=delete_id)
                blog.delete()
                messages.success(request, "Blog was deleted successfully ! Thank you for deleting useless or wrong blog !...")
                return redirect("blogs:index")
            else:
                messages.info(request, "We're sorry only super users can delete blogs !")
                return redirect("blogs:index")
        edit_id = request.GET.get("edit_id")
        if edit_id:
            blog = Blogs.objects.get(slug=edit_id)
            edit_form = BlogForm(instance=blog)
            return render(request, "index.html", {"form": form, "blogs": blogs, "edit_form": edit_form, "blog": blog})
        return render(request, "index.html", {"form": form, "blogs": blogs, "q": q, "count": count})
    
def edit_form(request, slug):
    blog = Blogs.objects.get(slug=slug)
    form = BlogForm(instance=blog, data=request.POST, files=request.FILES)
    if form.is_valid():
        if request.user.is_authenticated and request.user.is_superuser:
            form.save()
            messages.success(request, "Blog was changed successfully ! Thank you correcting any mistakes !...")
            return redirect("blogs:index")
        messages.info(request, "We're sorry only super users can edit blogs !")
        return redirect("blogs:index")