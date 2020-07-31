from django.shortcuts import render

# Create your views here.
from rest_framework import mixins,viewsets,status
from .models import UserInfo , UserTime
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class UserViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):

	queryset=UserInfo.objects.all()
	serializer_class=UserSerializer
	permission_classes=(AllowAny,)
	renderer_classes=[JSONRenderer,]
	def get_queryset(self):
		return self.queryset

	def list(self,request):
		serializer=self.serializer_class(self.get_queryset(),many=True)
		#serializer.is_valid(raise_exception=True)
		print(serializer.data)
		return Response(serializer.data,status=status.HTTP_200_OK)



