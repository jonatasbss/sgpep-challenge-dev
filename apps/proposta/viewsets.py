from rest_framework.viewsets import ModelViewSet
from .serializers import PropostaSerializer
from .models import Proposta
from .tasks import avaliar_prosposta


class PropostaViewSet(ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

    def perform_create(self, serializer):
        proposta = serializer.save()
        avaliar_prosposta.delay(proposta.id)
