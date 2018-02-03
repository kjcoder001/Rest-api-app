from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter # to display viewsets
from . import views

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')


urlpatterns=[
    url(r'^hello-view$',views.HelloApiView.as_view(),name='HelloApiView'),# .as_view --> to return this view as a view object
    url(r'',include(router.urls)), # if none of the urls match after /api/, the default page will show us the viewset
]
