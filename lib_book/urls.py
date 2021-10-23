from django.urls import path, include
from .views import getBooks,getcover, Addbook
urlpatterns = [
path('get/',getBooks.as_view()),
path('cover/',getcover.as_view()),
path('add/',Addbook.as_view()),
]
