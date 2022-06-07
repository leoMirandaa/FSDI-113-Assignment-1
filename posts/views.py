from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
  template_name= "posts/lists.html"
  model = Post

class PostDetailView(DetailView):
  template_name = "posts/detail.html"
  model = Post

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  template_name = "posts/new.html"
  model = Post
  fields = ['title', 'body']
  # fields = ['title', 'author', 'body']

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
    fields = ["title", "body"]

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