from django.urls import path
from stockapp import views

urlpatterns = [

    path('stocks/',views.StockList.as_view()),
    path('stocks/<symbol>/',views.StockDetail.as_view()),
    path('stocks/<symbol>/history/',views.StockHistoryDetail.as_view()),
    path('stocks/<symbol>/details/',views.StockDetailView.as_view(),name='details'),
]
