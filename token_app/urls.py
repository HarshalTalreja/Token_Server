from django.contrib import admin
from django.urls import path
from token_app import views

urlpatterns = [
    path('', views.index, name = 'token_app_index'),
    path('create/', views.create, name = 'create_new_pool'),
    path(r'^delete/(?P<token_key>\w+)/$', views.delete, name = 'delete'),
    path(r'^end/(?P<token_key>\w+)/$', views.end, name = 'end'),
]
