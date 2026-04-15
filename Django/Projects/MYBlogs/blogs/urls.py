from django.urls import path
from yarl import URL
from . import views


urlpatterns = [
    path('', views.blog_list, name='blog_list'),          # ✅ empty path
    path('<int:id>/', views.blog_detail, name='blog_detail'),
]