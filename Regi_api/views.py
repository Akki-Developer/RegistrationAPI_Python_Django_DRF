# from Regi_api.models import Adduser
from Regi_api.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    # permission_classes = (IsAuthenticated,)

     def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(
            {'success': 'True', 'message': 'User add successfully', 'user_id': serializer.data['user']},
            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)