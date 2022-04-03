from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

# Create your views here.

# class Home(ListView):
#     model = Post
#     template_name = 'home.html'

class Home(ListView):
    model = Post
    #queryset= Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:3]
    template_name = 'home.html'
    # def get_queryset(self):
    #     return Post.objects.all().order_by('likes')[:3]

    def get_context_data(self, **kwargs):
        data = super(Home, self).get_context_data(**kwargs)
        data['featured'] = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:3]
        data['latest'] = Post.objects.all().order_by('post_time').reverse()[:1]
        return data

class about(TemplateView):
    template_name = "about.html"

class PostView(LoginRequiredMixin ,DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Post, id= self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id= self.request.user.id).exists():
            liked = True
        data['num_of_like'] = likes_connected.total_like()
        data['post_is_liked'] = liked
        return data

class NewPost(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class EditPost(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class User_Profile(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'profile.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

def PostLike(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    if post.likes.filter(id= request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

class contact(TemplateView):
    template_name = "contact.html"

# class featured(ListView):
#     model = Post
#     queryset = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:3]
#     template_name = 'featured.html'
#     context_object_name = 'post_ordered'
