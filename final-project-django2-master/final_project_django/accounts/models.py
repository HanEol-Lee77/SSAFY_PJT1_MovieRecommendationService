from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings", blank=True)

    class Meta:
        ordering = ['-pk',]

class Preference(models.Model):
    # 각 장르에 대한 선호도 값
    genre1_like = models.FloatField()
    genre2_like = models.FloatField()
    genre3_like = models.FloatField()
    genre4_like = models.FloatField()
    genre5_like = models.FloatField()
    genre6_like = models.FloatField()
    genre7_like = models.FloatField()
    genre8_like = models.FloatField()
    genre9_like = models.FloatField()
    genre10_like = models.FloatField()
    genre11_like = models.FloatField()
    genre12_like = models.FloatField()
    genre13_like = models.FloatField()
    genre14_like = models.FloatField()
    genre15_like = models.FloatField()
    genre16_like = models.FloatField()
    genre17_like = models.FloatField()
    genre18_like = models.FloatField()

    # 국내/해외 영화에 대한 선호도 값
    nation1_like = models.FloatField()
    nation2_like = models.FloatField()

    # 각 관람등급에 대한 선호도 값(전체, 12세, 15세, 청불)
    watchgrade1_like = models.FloatField()
    watchgrade2_like = models.FloatField()
    watchgrade3_like = models.FloatField()
    watchgrade4_like = models.FloatField()

    # 상영시간에 대한 선호도 값(90분 이하, 90~120, 120~150, 150분 이상)
    time1_like = models.FloatField()
    time2_like = models.FloatField()
    time3_like = models.FloatField()
    time4_like = models.FloatField()