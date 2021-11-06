from copy import error
from typing import OrderedDict
from django.contrib.auth.models import User
from django.db.models import query
from django.db.models import Q
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from backend.settings import AUTH_PASSWORD_VALIDATORS

from lib_book.serializer import wiwSerializer
from .models import lib_bookModel, available, book_detail, whoIssuedWhat
from .custom_renderer import JPEGRenderer,PNGRenderer
import json

from django.db import connection

# Create your views here.

class getBooks(APIView):
    def get(self,req):
        #id title author genre total issued
        try:
            queryset = lib_bookModel.objects.order_by('-id').values('id','title','book_detail__author','book_detail__genre',
            'available__total','available__issued')[:int(req.query_params['number'])]
        except:
            return Response(error)
        return Response(queryset)

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


#if user has issued a book since every user can issue one copy of each book, therefore this check
class ifIssued(APIView):
    def get(self,req):

        #getting user_id using the auth_token
        cursor = connection.cursor()
        r = getUserId(req,cursor)

        uid = r[0]
        bid = int(req.query_params['book_id'])

        cursor.execute("select * from lib_book_whoissuedwhat where book_id_id = %d and user_id_id = %d"%(bid,uid))
        r = cursor.fetchall()
        if len(r) == 0:
            return Response({'issued':"0"})
        return Response({'issued':"1"})

#insert whoissuedwhat and update available table
class issue(APIView):
    def get(self,req):
        #insert into whoissuedwhat
        cursor = connection.cursor()
        uid = getUserId(req,cursor)[0]
        bid = int(req.query_params['book_id'])

        try:

            sql = "insert into lib_book_whoissuedwhat(book_id_id, user_id_id) values(%d,%d)"%(bid,uid)
            cursor.execute(sql)
            r = cursor.fetchone()
            print(r)

            #update the available table
            sql = "update lib_book_available set issued = issued + 1 where book_id_id = %d"%(bid)
            cursor.execute(sql)
            r = cursor.fetchone()
            print(r)
        except error:
            return Response({"status":"Not done due to some error"})
        return Response({"status":"Done"})

def getUserId(req,cursor):
        token = (req.headers['Authorization'].split(' ')[1])
        sql = "select user_id from authtoken_token as a where a.key = '%s'"%(token)
        cursor.execute(sql)
        return cursor.fetchone()# user_id = r[0]

#all the books issued by a user
class AllIssuedByUser(APIView):
    def get(self,req):
        cursor = connection.cursor()
        uid = getUserId(req,cursor)[0]

        sql = '''
        select b.id, b.title, w.book_id_id
        from lib_book_lib_bookmodel as b
        join
        lib_book_whoissuedwhat as w
        on b.id = w.book_id_id
        where w.user_id_id =%d;
        '''%(int(uid))

        cursor.execute(sql)
        r = cursor.fetchall()
        li = []
        for i in r:
            d = OrderedDict()
            d["id"]=i[0]
            d["title"]=i[1]
            d["book_id"]=i[2]
            li.append(d)
        # print(li)

        return Response(li)


#returning a book
class returnbook(APIView):
    def get(self,req):
        cursor = connection.cursor()
        uid = int(getUserId(req,cursor)[0])
        bid = int(req.query_params['book_id'])
        try:
            #delete entry from  whoissuedwhat table
            sql = '''
            delete from lib_book_whoissuedwhat
            where book_id_id = %d and user_id_id = %d
            '''%(bid,uid)

            cursor.execute(sql)
            r = cursor.fetchone()
            print(r)

            #update issued for book in available table
            sql = '''
            update lib_book_available
            set issued = issued - 1
            where book_id_id = %s
            '''%(bid)

            cursor.execute(sql)
            r = cursor.fetchone()
            print(r)
        except error:
            return Response(error)
        return Response({"status":"done"})

class createUser(APIView):
    permission_classes = [AllowAny]
    def post(self,req):
        username = req.data['username']
        email = req.data['email']
        password = req.data['password']
        first_name = req.data['first_name']
        last_name = req.data['last_name']

        try:
            user = User.objects.create_user(username,email,password,first_name=first_name,last_name=last_name)
            user.save()
        except error:
            return Response(error,status=401)
        return Response({"status":"Done"},status=200)