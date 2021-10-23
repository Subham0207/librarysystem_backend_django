from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class lib_bookModel(models.Model):
    title = models.CharField(max_length=100)
    coverImage = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class book_detail(models.Model):
    book_id = models.ForeignKey(lib_bookModel,on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)


class available(models.Model):
    book_id = models.ForeignKey(lib_bookModel,on_delete=models.CASCADE)
    total = models.IntegerField(default=4)
    issued = models.IntegerField(default=0)


class whoIssuedWhat(models.Model):
    book_id = models.ForeignKey(lib_bookModel,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
