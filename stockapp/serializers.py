from rest_framework import serializers
from .models import Stock,StockHistory


class StockSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id','symbol','name','marketcap','sector','industry')

class StockHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = StockHistory
        fields = ('id','open','high','low','close','date','stock')
