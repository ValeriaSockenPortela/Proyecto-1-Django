from django.urls import path
from .views import index, add, update, delete, contact, filter
app_name = 'comments'
urlpatterns = [
    path('add/', add, name='add'),
    path('contact/', contact, name='contact'),
    path('filter/', filter, name='filter'),
    path('', index, name='index'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete')
]
