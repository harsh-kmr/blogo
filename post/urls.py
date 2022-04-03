from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user_profile/', User_Profile.as_view(), name='user_profile'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', EditPost.as_view(), name='post_edit'),
    path('post/new/', NewPost.as_view(), name='post_new'),
    path('post/<int:pk>/',PostView.as_view(),name='post_detail'),
    path('post_like/<int:pk>/',PostLike,name='post_like'),
    path('contact/', contact.as_view(), name = 'contact'),
    path('about/',about.as_view(), name='about' ),
    path('', Home.as_view(), name='home'),
]