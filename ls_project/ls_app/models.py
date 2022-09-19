from secrets import choice
from django.db import models

beat_type = (("Free","Free"),("Buy","Buy"))
beat_genres = (("HipHop","HipHop"),("Dancehall","Dancehall"))

# Create your models here.
class beats(models.Model):
    """Model of beats."""
    beat_name = models.CharField(max_length=50, help_text="Enter beat name")
    producer = models.CharField(max_length=50, help_text="Enter producer name")
    artwork = models.ImageField(upload_to ='ls_app/media',help_text="Upload artwork")
    the_file = models.FileField(upload_to ='ls_app/media',help_text="Upload beat")
    genre = models.CharField(max_length=20, choices=beat_genres,default=1, help_text="Enter beat genre")
    beat_type = models.CharField(max_length=20, choices=beat_type, default=1, help_text="Enter beat Type")
    # Buy = models.BooleanField(verbose_name ='Buy', default=False)
    # Free = models.BooleanField(verbose_name ='Free', default=False)
    rel_date = models.DateField(help_text="Enter beat release date")
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.beat_name
        