from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class StreamingPlatform(models.Model):
    name = models.CharField(max_length= 50)
    about = models.TextField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name= 'Watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null = True)
    Watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name='Reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.rating) + ' | ' + self.Watchlist.title
    
    