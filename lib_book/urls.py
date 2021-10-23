from django.urls import path, include
from .views import getBooks
urlpatterns = [
path('get/',getBooks.as_view()),
]
