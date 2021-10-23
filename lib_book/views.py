from rest_framework.views import APIView
from rest_framework.response import Response
from .models import lib_bookModel
from .serializer import bookSerializer

# Create your views here.

class getBooks(APIView):
    def get(self,req):
        queryset = lib_bookModel.objects.all().order_by('-id')[:int(req.query_params['number'])]
        serializer = bookSerializer(queryset,many=True)
        return Response(serializer.data)