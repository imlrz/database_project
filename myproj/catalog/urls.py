from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    path('restaurants/<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('register', views.register, name='Registration'),
]

