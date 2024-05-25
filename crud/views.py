from django.views.generic import ListView,DetailView,TemplateView
from crud.models import Post
from django.http import HttpResponse
# Create your views here.


class BlogListView(ListView):

    model = Post
    template_name="home.html"


class BlogDetailView(DetailView):

    model = Post
    template_name= "post_detail.html"


class Consejos(TemplateView):

    template_name= "consejos.html"