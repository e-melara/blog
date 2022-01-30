from django.db import models

class FavoritosManager(models.Manager):
    def all_favoritos(self, usuario):
        return self.filter(
            entry__public=True,
            user_id=usuario
        ).order_by('created')
