from django.urls import path
from .views import PostListView, PostDetailView, RoomListView, RoomDetailView
from . import views

urlpatterns = [
    path('', RoomListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('contact_submit/', views.contact_submit, name='contact_submit'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
]