from stockapp.serializers import StockSerialzers, StockHistorySerializers
from stockapp.models import Stock,StockHistory
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import ListView, View


class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerialzers


class StockDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, symbol):
        try:
            return Stock.objects.get(symbol=symbol)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, symbol, format=None):
        stock = self.get_object(symbol)
        serializer = StockSerialzers(stock)
        return Response(serializer.data)

    def put(self, request, symbol, format=None):
        stock = self.get_object(symbol)
        serializer = StockSerialzers(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, symbol, format=None):
        stock = self.get_object(symbol)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StockHistoryDetail(APIView):
    """
    Retrieve History of Stock
    """
    def get_object(self, symbol):
        try:
            return Stock.objects.get(symbol=symbol)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, symbol, format=None):
        stock = self.get_object(symbol)
        history = stock.history.all()
        serializer = StockHistorySerializers(history,many=True)
        return Response(serializer.data)

    def put(self, request, symbol, format=None):
        stock = self.get_object(symbol)
        history = stock.history.all()
        request.data['stock'] = stock.pk
        serializer = StockHistorySerializers(history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockListView(ListView):
    model = Stock
    context_object_name = 'stock'
    template_name = 'home.html'
    paginate_by = 20

class StockDetailView(View):

    def render(self,request):
        return render(request,'stockdetail.html',{'stock':self.stock,'history':self.history})

    def get(self,request,symbol):
        self.stock = get_object_or_404(Stock,symbol=symbol)
        self.history = self.stock.history.all()
        return self.render(request)


