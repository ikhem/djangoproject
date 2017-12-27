from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'details/(?P<id>\d+)/$', views.details, name='details')
];