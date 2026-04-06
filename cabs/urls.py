from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='home'),
    path('book-taxi/', views.book_taxi, name='book_taxi'),
    path('success/', views.success, name='success'),
]
