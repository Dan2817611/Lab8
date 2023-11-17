from django.urls import path
from .views import index_page

urlpatterns = [
    path('index_page/', index_page, name='index_page'),
]