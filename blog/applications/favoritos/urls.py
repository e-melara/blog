from django.urls import path

from . import views

app_name = 'favorito_app'

urlpatterns = [
    path('perfil/', view=views.UserPageListView.as_view(), name='user-perfil'),
    path('add-favorites/<pk>/', view=views.AddFavorites.as_view(), name='add-favorite'),
    path('favorites-delete/<pk>/', view=views.FavoritesDeleteView.as_view(), name='delete-favorite'),
]
