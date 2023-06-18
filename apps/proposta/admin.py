from django.contrib import admin
from .models import Proposta
from django.db.models.signals import post_save
from .tasks import avaliar_proposta
from django.dispatch import receiver


# Register your models here.
@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'nome_completo', 'cpf', 'status')
    list_filter = ('status',)

    search_fields = ('nome_completo', 'cpf', 'status')
    ordering = ('nome_completo',)


@receiver(post_save, sender=Proposta)
def avaliar_proposta_nova(sender, instance, created, **kwargs):
    if created:
        avaliar_proposta.delay(instance.id)


post_save.connect(avaliar_proposta_nova, sender=Proposta)
