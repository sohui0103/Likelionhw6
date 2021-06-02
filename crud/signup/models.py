from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pub_date = models.DateTimeField()
    email = models.EmailField(max_length=100)
    introduce = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]