from django.db import models

# Create your models here.
class Link(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)
    stringname = models.CharField(max_length=200, blank=True, null=True)

    # def __str__(self) :
    #     return self.stringname
    