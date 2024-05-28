from django.urls import path
from catalog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    path('restaurants/<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('dishes/', views.DishListView.as_view(), name='dishes'),
    path('dishes/<int:pk>', views.DishDetailView.as_view(), name='dish-detail'),
    path('register', views.register, name='Registration'),
    path('adddishes/', views.adddishes, name='adddishes'),
    path('adddishes_form/', views.adddishes_form, name='adddishes_form'),
    path('editrestaurants/<int:pk>', views.editrestaurants, name='editrestaurants'),
    path('comment/<int:pk>', views.add_comment, name='add-comment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


