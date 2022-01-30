from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='home',
    ),
    path(
        'register-suscription/', 
        views.SuscripberCreateView.as_view(),
        name='add-suscription',
    ),  
]