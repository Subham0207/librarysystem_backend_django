from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# Create your views here.


class demoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,req):
        return Response({'status':'Authenticated user verification'})
        