from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from crud.models import Post
from django.http import HttpResponse

from django.urls import reverse_lazy
# Create your views here.


class BlogListView(ListView):

    model = Post
    template_name="home.html"


class BlogDetailView(DetailView):

    model = Post
    template_name= "post_detail.html"

class BlogCreateView(CreateView):

    model= Post

    template_name= "post_new.html"

    fields=["title","body","author"]

    success_url = reverse_lazy("home")


class BlogUpdateView(UpdateView):

    model=Post

    template_name= "post_edit.html"

    fields = ["title","body"]

    success_url = reverse_lazy("home")


class BlogDeleteView(DeleteView):

    template_name= "post_delete.html"

    model= Post

    success_url = reverse_lazy("home")



class Consejos(TemplateView):

    template_name= "consejos.html"