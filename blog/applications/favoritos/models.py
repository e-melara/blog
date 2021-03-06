from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel

from applications.entrada.models import Entry
from .managers import FavoritosManager

class Favorites(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )
    
    objects = FavoritosManager()
    
    class Meta:
        unique_together = ('user', 'entry') # para que no se repita una entrada en la db del mismo usuario
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas'
    
    def __str__(self):
        return self.entry.title