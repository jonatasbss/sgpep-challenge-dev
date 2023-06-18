from django.urls import path
from apps.proposta import views

app_name = 'proposta'

urlpatterns = [
    path('', views.PropostaListView.as_view(), name='list_propostas'),
    path('nova-proposta/', views.PropostaCreateViewAPI.as_view(), name='create_proposta')
]
