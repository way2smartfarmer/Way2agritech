from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #Identifying an type of the object User likes
    object_id = models.PositiveIntegerField()   #Referencing a perticular object
    content_object = GenericForeignKey()   #Reading an Actual Object
