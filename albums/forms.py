from django import forms 
from .models import Album, Cover, album, cover

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'year_released',
            'genre',
            'mood',
        ]
        
class CoverForm(forms.ModelForm):
    class Meta:
        model = Cover
        fields = [
            'image',
        ]