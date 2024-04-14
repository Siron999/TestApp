from django.urls import path
from .views import index
urlpatterns = [
    path('file/<int:id>', index, name='home')
]
