from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Favorites
from applications.entrada.models import Entry

class UserPageListView(LoginRequiredMixin, ListView):
    context_object_name = 'entradas_user'
    template_name = "favoritos/perfil.html"
    login_url = reverse_lazy('users_app:user-login')
    
    def get_queryset(self):
        return  Favorites.objects.all_favoritos(self.request.user)
    
    
class AddFavorites(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')
    
    def post(self, request, *args, **kargs):
        usuario = self.request.user
        entry = Entry.objects.get(id=self.kwargs['pk'])
        
        Favorites.objects.create(
            user=usuario,
            entry=entry
        )
        
        return HttpResponseRedirect(
            reverse('favorito_app:user-perfil')
        )
        

class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favorito_app:user-perfil')
