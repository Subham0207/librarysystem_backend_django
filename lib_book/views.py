from rest_framework.views import APIView
from rest_framework.response import Response
from .models import lib_bookModel, available, book_detail
from .serializer import bookSerializer
from .custom_renderer import JPEGRenderer,PNGRenderer
import json

# Create your views here.

class getBooks(APIView):
    def get(self,req):
        queryset = lib_bookModel.objects.all().order_by('-id')[:int(req.query_params['number'])]
        serializer = bookSerializer(queryset,many=True)
        return Response(serializer.data)

class getcover(APIView):
    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self,req):
        queryset = lib_bookModel.objects.get(id=req.query_params['id']).coverImage
        return Response(queryset)


class Addbook(APIView):
    def post(self,req):
        #title,coverimage, author, description, genre
        book = lib_bookModel(title=req.data['title'],coverImage=req.data['coverimage'])
        book.save()

        bookdetail = book_detail(book_id=book,author=req.data['author'],description=req.data['description'],genre=req.data['genre'])
        bookdetail.save()

        avail = available(book_id=book)
        avail.save()
    
        return Response({'status':'Successfully Inserted'})