from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from heros.models import HeroModel


class HeroUpdate(forms.ModelForm):
    challenge_rate =forms.IntegerField(label='', validators=[MinValueValidator(0), MaxValueValidator(3)])
    class Meta:
        model = HeroModel
        fields = ['challenge_rate',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
