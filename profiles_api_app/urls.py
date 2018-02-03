from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^hello-view$',views.HelloApiView.as_view(),name='HelloApiView'),# .as_view --> to return this view as a view object
]
