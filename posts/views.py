from typing import List
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post

class PostListView(LoginRequiredMixin,ListView):
  template_name= "posts/lists.html"
  model = Post

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    #add in a QuerySet of al lbooks
    context['post_list'] = Post.objects.filter(
      is_private=False).order_by('created_on').reverse()
    return context
    # context['post_list'] = Post.objects.filter(
    #   author=self.request.user).order_by('created_on').reverse()
    # return context


class PrivatePostListView(LoginRequiredMixin, ListView):
  template_name = "posts/private_list.html"
  model = Post

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['post_list'] = Post.objects.filter(
      is_private=True).filter(
        author=self.request.user).order_by('created_on').reverse()
    return context
    #     is_private=True).filter(
    #       author=self.request.user).order_by('created_on').reverse()
    # return context

class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
  template_name = "posts/detail.html"
  model = Post

  def test_func(self):
    post = self.get_object()
    if post.is_private:
      return post.author == self.request.user
    return True

class PostCreateView(LoginRequiredMixin, CreateView):
  template_name = "posts/new.html"
  model = Post
  fields = ['title', 'body', 'is_private']

  def form_valid(self, form): #form = form obj, this happens whtn the form is submited from html
    form.instance.author = self.request.user
    return super().form_valid(form) #returning the call from the superclass(createview)

  def test_func(self):
    return self.request.user.is_staff #true=continue/false=redirect

#like createView,also a form,
# #will return an instance of the post, it will need pk through the urlpatterns
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "body", "is_private"]

    def test_func(self):
      post = self.get_object()
      return post.author == self.request.user

#need pk(target)
#will return a form, its a confirmation form. act
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
      post = self.get_object()
      return post.author == self.request.user

# UserPassesTestMixin update user that created the psots