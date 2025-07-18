from django.urls import path
from .views import add, index, update, delete

app_name = 'comments'
urlpatterns = [
    path('/add/', add, name='add'),
    path('', index, name='index'),
    path('/update/<int:pk>/', update, name='update'),
    path('/delete/<int:pk>/', delete, name='delete')
]
