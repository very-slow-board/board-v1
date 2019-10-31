from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Board
from .serializers import BoardListSerializer, BoardDetailSerializer
from core.permissions import IsGetOrIsAuthenticated


class BoardListView(APIView):
    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, request, format=None):
        """
        게시판 리스트
        ---
        parameters:
         -
        ---
        returns:
         - items
           - pk
           - title
        ---
        status:
         - HTTP_200_OK
        """

        qs = Board.objects.all()
        serializer = BoardListSerializer(qs, many=True)
        data = {'msg': 'success', 'items': serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)


class BoardDetailView(APIView):
    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, request, pk, format=None):
        """
        게시판 상세
        ---
        parameters:
         -
        ---
        returns:
         - item
           - pk
           - title
           - content
        ---
        status:
         - HTTP_200_OK
        """
        board = get_object_or_404(Board, pk=pk)
        serializer = BoardDetailSerializer(board)
        data = {'msg': 'success', 'item': serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)
