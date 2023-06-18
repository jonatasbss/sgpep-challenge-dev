from celery import shared_task
from .models import Proposta
from django.shortcuts import get_object_or_404
from random import randint


@shared_task
def avaliar_prosposta(proposta_id):
    proposta = get_object_or_404(Proposta, id=proposta_id)
    if randint(0, 1) == 0:
        proposta.status = 'Aprovado'
    else:
        proposta.status = 'Reprovado'
    proposta.save()
