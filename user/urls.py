from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^view/(?P<username>\w+)/$', views.profile, name='profile'),
]
