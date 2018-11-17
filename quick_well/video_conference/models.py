from django.db import models

# Create your models here.
class User(models.Model):
    User_id =
 class video_con_request(models.Model):
     user = models.ManyToManyField(User_id)