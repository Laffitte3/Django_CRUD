from django.urls import path
from crud.views import BlogListView


urlpatterns=[

    path("",BlogListView.as_view(),name="home"),

]

