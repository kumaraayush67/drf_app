from django.db import models

class User(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    email = models.EmailField()
    web = models.URLField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    @property
    def name(self):
        return self.first_name + ' ' + self.last_name
