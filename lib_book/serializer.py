from django.db.models import fields
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from lib_book.models import lib_bookModel, whoIssuedWhat


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = lib_bookModel
        fields = ['id','title']


class wiwSerializer(serializers.ModelSerializer):
    class Meta:
        model = whoIssuedWhat
        fields = ['user_id','book_id']