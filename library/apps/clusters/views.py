from django.shortcuts import render


#crud 

#list books paginado

# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .models import Clusters
from .serializer import serializerCluster
from ..livros.serializer import serializerBook
from ast import Pass
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json 
from rest_framework.permissions import IsAuthenticated



class ClusterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Clusters.objects.select_related('user').all()
    serializer_class = serializerCluster
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





class ClusterApi(APIView):
    permission_classes = [IsAuthenticated]

    @require_http_methods(["GET"])
    def ClusterAPI_Consult(request):
        id = request.GET.get('id', None)
        
        if id is None:
            return JsonResponse({'error': 'error: Envie um id valido'}, status=404)
        try:
            id_int = int(id)
        except ValueError:
            return JsonResponse({'error': 'error: ID inválido'}, status=400)

        try:
            Cluster = Clusters.objects.get(id=id_int)
            list_books = Cluster.books.all()
            data = []

            for book in list_books:
                book_serialized = serializerBook(book)
                data.append(book_serialized.data if hasattr(book_serialized, 'data') else book_serialized)
                
            return JsonResponse({'data': data}, status=200)
        
        except Clusters.DoesNotExist:
            return JsonResponse({'error': 'error: Grupo não encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'message: {e}', 'status': 500})
      
        
    


