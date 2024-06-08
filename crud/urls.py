from django.urls import path
#Views
from crud.views import BlogListView
from crud.views import Consejos
from crud.views import BlogDetailView
from crud.views import BlogCreateView
from crud.views import BlogUpdateView
from crud.views import BlogDeleteView

#statics
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[

    path("",BlogListView.as_view(),name="home"),
    path("consejo",Consejos.as_view(),name="consejos"),
    path("post/<int:pk>/",BlogDetailView.as_view(),name="detail"),
    path("post/new/",BlogCreateView.as_view(),name="post_new"),
    path("post/<int:pk>/edit",BlogUpdateView.as_view(),name="post_edit"),
    path("post/<int:pk>/delete",BlogDeleteView.as_view(),name="post_delete"),
    #path()


]

#Configuracion cargar imagenes
#if settings.DEBUG == True:

    #from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
