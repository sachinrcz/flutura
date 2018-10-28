from rest_framework import serializers
from .models import Stock


class StockSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id','symbol','name','marketcap','sector','industry')