from django.views.generic import ListView
from crud.models import Post
from django.http import HttpResponse
# Create your views here.


class BlogListView(ListView):

    model = Post
    template_name="home.html"

def Consejos(request):

    return HttpResponse("consejos.html")
    