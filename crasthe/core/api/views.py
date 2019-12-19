from rest_framework import generics, status
from rest_framework.response import Response

class StatusApiView(generics.GenericAPIView):

    def get(self,request,*args, **kwargs):
        return Response({'status': 'ok'},status=status.HTTP_200_OK)