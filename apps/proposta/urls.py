from django.urls import path
from apps.proposta import views

urlpatterns = [
    path('propostas/', views.PropostaListView.as_view(), name='list_propostas'),
    path('nova-proposta/', views.PropostaCreateViewAPI.as_view(), name='create_proposta')
]
