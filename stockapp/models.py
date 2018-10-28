from django.db import models

# Create your models here.


class Stock(models.Model):
    symbol = models.CharField(max_length=10,blank=False)
    name = models.CharField(max_length=100,blank=True,default='')
    marketcap = models.DecimalField(default=0,decimal_places=1,max_digits=10)
    sector = models.CharField(max_length=100,blank=True,default='')
    industry = models.CharField(max_length=100,blank=True,default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)