from django.urls import path, include
from .views import getBooks,getcover
urlpatterns = [
path('get/',getBooks.as_view()),
path('cover/',getcover.as_view()),
]
