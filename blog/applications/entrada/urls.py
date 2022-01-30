from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path(
        'entradas/', 
        views.EntryListView.as_view(),
        name='entrada-all',
    ),
    path(
        'entradas/<pk>/', 
        views.EntryDetailView.as_view(),
        name='entrada-detail',
    ),
]