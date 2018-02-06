from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter # to display viewsets
from . import views

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)# django knows implicitly about the base_name because its a ModelViewSet!
router.register('login',views.LoginViewSet,base_name='login')# this viewset doesn't correspond to any model ViewSet
# hence its imperative that we mention a base_name
router.register('feed',views.UserProfileFeedViewSet) # a ModelViewSet , no base_name required

urlpatterns=[
    url(r'^hello-view$',views.HelloApiView.as_view(),name='HelloApiView'),# .as_view --> to return this view as a view object
    url(r'',include(router.urls)), # if none of the urls match after /api/, the default page will show us the viewset

]
