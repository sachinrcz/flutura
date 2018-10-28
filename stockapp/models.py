from django.db import models

# Create your models here.


class Stock(models.Model):
    symbol = models.CharField(max_length=10,blank=False)
    name = models.CharField(max_length=100,blank=True,default='')
    marketcap = models.DecimalField(default=0,decimal_places=3,max_digits=20)
    sector = models.CharField(max_length=100,blank=True,default='')
    industry = models.CharField(max_length=100,blank=True,default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol

    class Meta:
        ordering = ('name',)


class StockHistory(models.Model):
    date = models.DateField(blank=False)
    open = models.DecimalField(default=0,decimal_places=4,max_digits=20)
    low = models.DecimalField(default=0,decimal_places=4,max_digits=20)
    high = models.DecimalField(default=0,decimal_places=4,max_digits=20)
    close = models.DecimalField(default=0,decimal_places=4,max_digits=20)
    volume = models.DecimalField(default=0,decimal_places=4,max_digits=20)
    stock = models.ForeignKey(Stock,related_name='history',on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}-{}'.format(self.stock.symbol, self.date)

    class Meta:
        ordering = ('-date',)
