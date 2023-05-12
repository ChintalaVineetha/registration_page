from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home),
    path('Register',views.registration),
    path('Display', views.disp),
    path('verify',views.verify),
    path('view', views.viewdetails),
    path('edit', views.edit),
]