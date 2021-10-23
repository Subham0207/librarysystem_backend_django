from django.contrib import admin
from .models import lib_bookModel,book_detail,available,whoIssuedWhat

# Register your models here.
admin.site.register(lib_bookModel)
admin.site.register(book_detail)
admin.site.register(available)
admin.site.register(whoIssuedWhat)