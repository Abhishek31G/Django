from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name
    

class State(models.Model):
    state_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    
    def __str__(self):
        return self.state_name