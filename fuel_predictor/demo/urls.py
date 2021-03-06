from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('fuel_quote', views.fuel_quote, name='fuel_quote'),
    path('fuel_hist', views.fuel_hist, name='fuel_hist'),
    path('client_profile', views.client_profile, name='client_profile'),
    path('admin', views.admin, name='admin'),
    path('logout', views.logout, name='logout')
]
