from django.urls import path, include
from .views import AllIssuedByUser, createUser, getBooks,getcover, Addbook, ifIssued, issue, returnbook
urlpatterns = [
path('get/',getBooks.as_view()),
path('cover/',getcover.as_view()),
path('add/',Addbook.as_view()),
path('ifissued/',ifIssued.as_view()),
path('issue/',issue.as_view()),
path('AllIssued/',AllIssuedByUser.as_view()),
path('returnbook/',returnbook.as_view()),
path('register/',createUser.as_view()),
]
