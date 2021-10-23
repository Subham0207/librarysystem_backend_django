from django.db.models import fields
from rest_framework import serializers
from .models import lib_bookModel


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = lib_bookModel
        fields = ['id','title','is_issued','author']
