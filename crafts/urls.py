from django.urls import path
from .views import artisan_signup, customer_signup, add_product, homepage, artisan_login, customer_login, logout_view

urlpatterns = [
    path('', homepage, name='home'),
    path('signup/artisan/', artisan_signup, name='artisan_signup'),
    path('signup/customer/', customer_signup, name='customer_signup'),
    path('login/artisan/', artisan_login, name='artisan_login'),
    path('login/customer/', customer_login, name='customer_login'),
    path('add_product/', add_product, name='add_product'),
    path('logout/', logout_view, name='logout'),

]
