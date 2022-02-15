from django.contrib.auth.models import User
from django.db import models

# Create your models here.


#! Adding New Fields to Default User by Using AbstractUser
# * Mevcut default user'a ilave field eklemek için AbstractUser'ı kullanıyoruz. Default user'a ilave olarak iki tane field ekliyoruz.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(
        upload_to='profile_pics', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
