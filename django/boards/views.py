from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Board
from .serializers import BoardListSerializer
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
         - code
           - 200: 완료
         - boards (펫톡 객체 리스트)
           - pk
           - type
           - title
           - content
           - view_count
           - created_at
           - user
             - pk
             - nick_name
             - profile_image
           - images
             - image_url
           - comments
             - pk
             - content
             - created_at
             - user (comment 작성자 객체 정보)
               - pk
               - nick_name
               - profile_image
        ---
        status:
         - HTTP_200_OK
        """

        qs = Board.objects.all()
        serializer = BoardListSerializer(qs, many=True)
        data = {'msg': 'success', 'items': serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)
