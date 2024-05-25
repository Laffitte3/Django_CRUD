from django.urls import path
#Views
from crud.views import BlogListView
from crud.views import Consejos
from crud.views import BlogDetailView

#statics
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[

    path("",BlogListView.as_view(),name="home"),
    path("consejo",Consejos.as_view(),name="consejos"),
    path("post/<int:pk>/",BlogDetailView.as_view(),name="detail"),

]

#Configuracion cargar imagenes
#if settings.DEBUG == True:

    #from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
