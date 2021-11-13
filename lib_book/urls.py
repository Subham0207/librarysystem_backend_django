from django.urls import path, include
from .views import AllIssuedByUser, createUser, getBooks,getcover, Addbook, ifIssued, issue, returnbook,getUserName, searchbooks, reload, serveDetails
urlpatterns = [
path('get/',getBooks.as_view()),
path('cover/',getcover.as_view()),
path('add/',Addbook.as_view()),
path('ifissued/',ifIssued.as_view()),
path('issue/',issue.as_view()),
path('AllIssued/',AllIssuedByUser.as_view()),
path('returnbook/',returnbook.as_view()),
path('register/',createUser.as_view()),
path('getusername/',getUserName.as_view()),
path('search/',searchbooks.as_view()),
path('getavailabilty/',reload.as_view()),
path('serveDetails/',serveDetails.as_view()),
]
