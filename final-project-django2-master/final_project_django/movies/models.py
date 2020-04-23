from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    summary = models.TextField(blank=True)
    directorNm = models.CharField(max_length=45, blank=True)
    genresCds = models.ManyToManyField(Genre, related_name="movies", blank=True)
    # genresNm = models.CharField(max_length=150)
    prdtYear = models.IntegerField(blank=True, null=True)
    openDt = models.IntegerField(blank=True, null=True)
    showTm = models.IntegerField(blank=True, null=True)
    nationNm = models.CharField(max_length=45, blank=True, null=True)
    actorsNm = models.CharField(max_length=150, blank=True, null=True)
    watchGradeNm = models.CharField(max_length=100, blank=True, null=True)
    companyNmDict = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=300, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)
    userRating = models.CharField(max_length=45, blank=True, null=True)
    audiAcc = models.CharField(max_length=45, blank=True, null=True)
    thumbsNm = models.CharField(max_length=500, blank=True, null=True)
    thumbsImage = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    comment = models.TextField()
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=False)

    class Meta:
        ordering = ['-pk',]

    def __str__(self):
        return f'{self.score} {self.comment}'