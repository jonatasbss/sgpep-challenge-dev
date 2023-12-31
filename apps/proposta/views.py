from datetime import timedelta

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Proposta
from .serializers import PropostaSerializer
from .tasks import avaliar_proposta
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class PropostaListView(TemplateView):
    template_name = 'proposta/list-proposta.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['propostas'] = Proposta.objects.all()
        context['aprovadas'] = Proposta.objects.filter(status='Aprovado')
        context['reprovadas'] = Proposta.objects.filter(status='Reprovado')
        context['em_analise'] = Proposta.objects.filter(status='Em Análise')
        return context


# class PropostaListViewAPI(generics.ListAPIView):
#     queryset = Proposta.objects.all()
#     serializer_class = PropostaSerializer


@method_decorator(login_required, name='dispatch')
class PropostaCreateViewAPI(CreateModelMixin, generics.GenericAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

    def perform_create(self, serializer):
        proposta = serializer.save()
        avaliar_proposta.delay(proposta.id)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
