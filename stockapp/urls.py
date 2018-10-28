from django.urls import path
from stockapp import views

urlpatterns = [
    path('stocks/',views.StockList().as_view()),
    path('stocks/<int:pk>/',views.StockDetail().as_view()),
]
