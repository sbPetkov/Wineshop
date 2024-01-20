from itertools import product

from django.urls import path

from shop.views import home, about, login_user, logout_user, register_user, wine, category, category_summery, update_user

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('update_user/', update_user, name='update_user'),
    path('wine/<int:pk>', wine, name='wine'),
    path('category/<str:pk>', category, name='category'),
    path('category/summery/', category_summery, name='category_summery')
]