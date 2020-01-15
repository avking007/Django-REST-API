from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='Hello-viewset')
router.register('profile-viewset', views.UserProfileViewSet)
router.register('feed', views.ProfileFeedViewSet)
urlpatterns = [
    path('hello-view/', views.HelloApi.as_view(), name='api'),
    path('',include(router.urls)),
    path('login/', views.UserLoginApi.as_view()),
]
