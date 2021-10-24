from django.db.models import fields
from rest_framework import serializers
from lib_book.models import lib_bookModel


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = lib_bookModel
        fields = ['id','title']
