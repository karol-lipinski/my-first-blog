from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
#from datetime import datetime
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    paginator = Paginator(posts, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'page': page, 'posts': post_list, 'page_range':paginator.page_range})
    
   #return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    today = timezone.now().strftime("%x") == post.published_date.strftime("%x")
    return render(request, 'blog/post_detail.html', {'post': post, 'today':today})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    today = timezone.now().strftime("%x") == post.published_date.strftime("%x")
    if not today:
        return render(request, 'blog/post_detail.html', {'post': post, 'today':today})
    
      
    elif request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
