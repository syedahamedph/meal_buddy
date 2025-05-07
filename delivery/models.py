from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    picture = models.URLField(max_length=200,default='https://imgs.search.brave.com/v36PCp-pIlb_intMyKbdO378ka5ET7s0aknZFGohom0/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9kM2gx/bGcza3N3Nmk2Yi5j/bG91ZGZyb250Lm5l/dC9tZWRpYS9pbWFn/ZS8yMDE4LzA2LzE0/L2M3YmMwYWYzZmNk/YTQ4ZTQ5NzRjYWJm/NGQyZTAxNjA4X0FT/UF9MYW5nb3VzdGlu/ZUF1TWllbChjKUpl/YW5NaWNoZWxEZWxN/b3JhbC5qcGc')
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()
   
