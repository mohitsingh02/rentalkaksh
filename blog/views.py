from django.shortcuts import render
from .models import Post, Contact, Room
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def contact_submit(request):
    uname = request.POST["cust_name"]
    phone = request.POST['cust_phone']
    rad = request.POST['gridRadios']
    email = request.POST['cust_email']
    text = request.POST['cust_text']

    detail = Contact(UName=uname, Phone=phone, email=email, rad=rad, text=text)
    detail.save()
    return render(request, 'blog/home.html')


# def blog(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/blog.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post


class RoomListView(ListView):
    model = Room
    template_name = 'blog/home.html'
    context_object_name = 'rooms'
    paginate_by = 2


class RoomDetailView(DetailView):
    model = Room


def search(request):
    query = request.GET['search']
    allroomslocation = Room.objects.filter(location__icontains=query)
    allroomsnoroom = Room.objects.filter(no_room__icontains=query)
    allrooms = allroomslocation.union(allroomsnoroom)
    params = {'allrooms': allrooms, 'query': query}
    return render(request, 'blog/search.html', params)


