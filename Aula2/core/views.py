from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer

class ListaTarefasAPIView(APIView):
    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()

        serializer = TarefaSerializer(tarefas, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ContagemTarefasAPIView(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas
        return Response(    {
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes
        }   )
