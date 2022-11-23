from django.db import models
from django.urls import reverse

# Create your models here.

class Musician (models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name+" "+self.last_name

    def  get_absolute_url (self):
        return reverse('class_app:indexList')


class Album(models.Model):
    artist=models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albumList')
    name=models.CharField(max_length=50)
    release_date=models.DateField()

    rating=(
    (1,"Worst"),
    (2,"Bad"),
    (3,"Not Bad"),
    (4,"Good"),
    (5,"Excellent"),

    )
    num_stars=models.IntegerField(choices=rating)
    def __str__(self):
        return self.name+" Rating: "+str(self.num_stars)
