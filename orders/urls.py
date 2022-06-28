from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_create, name='create'),
    path('', views.order_create, name='created'),
]
