from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        ZOUGLOU = 'ZG'
    name = models.CharField(max_length=100)
    biography = models.CharField(max_length=1000)
    genre = models.CharField(choices=Genre.choices, max_length=5)
    year_formed = models.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'RC'
        CLOTHINGS = 'CL'
        POSTERS = 'PT'
        MISCELLANEOUS = 'MS'
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(null=True, blank=True)
    type = models.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title