from rest_framework import generics, status
from rest_framework.response import Response

class GetHorariosApiView(generics.GenericAPIView):

	def get(self,request,*args, **kwargs):
		horarios = ['9:00', '10:00', '11:00', '12:00']
		return Response({'horarios': horarios}, status=status.HTTP_200_OK)