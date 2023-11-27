from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms


# Create your models here.

class HeroModel(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=512)
    challenge_rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])

    class Meta:
        ordering = ('-challenge_rate',)

    def rate_string(self):
        return range(self.challenge_rate)

    def hero_count(self):
        return self.HeroModel.object.all().count


    def __str__(self):
        return f'{self.name}: {self.challenge_rate}'







