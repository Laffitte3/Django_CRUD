from django.urls import path
from crud.views import BlogListView
from crud.views import Consejos
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[

    path("",BlogListView.as_view(),name="home"),
    path("",Consejos,name="consejos")

]

#Configuracion cargar imagenes
#if settings.DEBUG == True:

    #from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
