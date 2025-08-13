from django.urls import path
from rest_framework import routers

from .viewsets import  ElementReadOnlyViewSet, ElementCreateUpdateDestroyViewSet, CategoryViewSet, TypeViewSet, CommentViewSet
from . import views
route = routers.SimpleRouter()

route.register('elementRead',ElementReadOnlyViewSet, basename='element-read')
route.register('elementUpdate',ElementCreateUpdateDestroyViewSet, basename='elment-update')
route.register('category',CategoryViewSet)
route.register('type',TypeViewSet)
route.register('comment',CommentViewSet)


urlpatterns = route.urls

urlpatterns += path('login', views.login, name='login'),