from django.db import models
from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    description = models.TextField()
    title = models.CharField("Nombre", max_length=30)
    about = models.CharField("Titulo Nosotros", max_length=50)
    about_text = models.TextField()
    contact_email = models.EmailField(
        "email de contacto", blank=True, null=True)
    phone = models.CharField("Telefono de contacto", max_length=50)

    class Meta:
        verbose_name = "Pagina Principal"
        verbose_name_plural = "Pagina Principal"

    def __str__(self):
        return self.title


class Suscribers(TimeStampedModel):
    email = models.EmailField()
    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural =  "Suscriptores"
        
    def __str__(self):
        return self.email
