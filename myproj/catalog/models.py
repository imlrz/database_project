from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class USER(models.Model):
    user_ID = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    def generate_user_ID(self):
        from django.db.models import F, Max
        prefix = 'CT'
        max_id = USER.objects.aggregate(max_id = Max('user_ID'))['max_id']
        if max_id is None:
            max_id = 0
        id_number = max_id + 1
        return f'{prefix: 0>2}{id_number: 0>8}'
    
    def __str__(self):
        return f'{self.user_ID}'


class RESTAURANT(models.Model):
    resta_ID = models.AutoField(primary_key = True)
    resta_name = models.CharField(max_length = 20)
    location = models.CharField(max_length = 1)
    time_open = models.TimeField()
    time_close = models.TimeField()
    manager = models.ForeignKey('USER', models.SET_NULL, blank = True, null = True)
    tag = models.CharField(max_length = 4)
    AVG_grade = models.FloatField()
    more_Info = models.CharField(max_length = 200)
    #image = models.ImageField

    def generate_resta_ID(self):
        from django.db.models import F, Max
        prefix = 'RT'
        max_id = USER.objects.aggregate(max_id = Max('resta_ID'))['max_id']
        if max_id is None:
            max_id = 0
        id_number = max_id + 1
        return f'{prefix: 0>2}{id_number: 0>8}'
    
    def __str__(self):
        return f'{self.resta_ID}'
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('restaurant-detail', args=[str(self.resta_ID)])


