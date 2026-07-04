from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destinations/create/', views.destination_create, name='destination_create'),
    path('destinations/<slug:slug>/', views.destination_detail, name='destination_detail'),
    path('destinations/<slug:slug>/edit/', views.destination_update, name='destination_update'),
    path('destinations/<slug:slug>/delete/', views.destination_delete, name='destination_delete'),
    path('destinations/<slug:slug>/vote/<str:vote_type>/', views.vote_destination, name='vote_destination'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
