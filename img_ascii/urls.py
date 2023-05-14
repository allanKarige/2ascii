from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path('upload/', views.upload_page, name='upload'),
]
