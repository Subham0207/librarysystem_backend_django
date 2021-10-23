from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class lib_bookModel(models.Model):
    title = models.CharField(max_length=100)
    tags = models.TextField()
    photo = models.ImageField(upload_to='images/')
    is_issued = models.BooleanField(default=False)
    author = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.title