from django.shortcuts import render
from rest_framework.views import APIView

from api.pagination import PaginacaoVagas
from api.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


erroServidor = JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VagaList(APIView):
    def get(self, request):
        try:
            lista_vagas = Vaga.objects.all()
            paginator = PaginacaoVagas()
            result_page = paginator.paginate_queryset(lista_vagas, request)
            serializer = VagaSerializer(result_page, many=True)
            return  paginator.get_paginated_response(serializer.data)
        except Exception:
            return erroServidor

    def post(self, request):
        try:
            serializer = VagaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return erroServidor



class VagaDetalhes(APIView):
    def get(self, request, pk=None):
        try:
            if pk =="0":
                return  JsonResponse({'mensagem':"O id deve ser maior que zero"},
                                     status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga)
            return  Response(serializer.data)
        except Vaga.DoesNotExist:
            return JsonResponse({'mensagem': "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return erroServidor

    def put(self,request, pk=None):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                    status= status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return  Response(serializer.errors,
                             status=status.HTTP_400_BAD_REQUEST)
        except Vaga.DoesNotExists:
            return JsonResponse({'mensagem': "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return erroServidor

    def delete(self, request, pk=None):
        try:
            if pk == "0":
                return  JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                     status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            vaga.delete()
            return  Response(status=status.HTTP_204_NO_CONTENT)
        except Vaga.DoesNotExists:
            return JsonResponse({'mensgem':"A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return erroServidor


