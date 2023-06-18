from django.contrib import admin
from .models import Proposta


# Register your models here.
@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'status')
    list_filter = ('status',)

    search_fields = ('nome_completo', 'cpf', 'status')
    ordering = ('nome_completo',)
