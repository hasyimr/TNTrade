from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('coin/<str:code>/', views.coin, name='coin'),
    path('purchase/', views.purchase, name='purchase'),
    path('profile/', views.profile, name='profile'),
    path('sell/', views.sell, name='sell')
]
