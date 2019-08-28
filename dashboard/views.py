from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from . import dataparse

def addToDb(Ticker, PercentChange30, PercentChange365, PercentChange, Change, WeekHigh52, WeekLow52, LastTradedPrice, High, Low, Open, TradedValInCrs, TradedValInLacs):
    "Adds/Updates a single set of stock details to the database"
    print(Ticker, PercentChange30, PercentChange365, PercentChange, Change, WeekHigh52, WeekLow52, LastTradedPrice, High, Low, Open, TradedValInCrs, TradedValInLacs)
    try:
        t = models.stock.objects.get(Symbol=Ticker)
        t.PercentChange30=PercentChange30
        t.PercentChange365=PercentChange365
        t.PercentChange=PercentChange
        t.Change=Change
        t.WeekHigh52=WeekHigh52
        t.WeekLow52=WeekLow52
        t.LastTradedPrice=LastTradedPrice
        t.High=High
        t.Low=Low
        t.Open=Open
        t.TradedValInCrs=TradedValInCrs
        t.TradedValInLacs=TradedValInLacs
        t.save()

    except models.stock.DoesNotExist:
        t=models.stock()
        t.Symbol=Ticker
        t.PercentChange30=PercentChange30
        t.PercentChange365=PercentChange365
        t.PercentChange=PercentChange
        t.Change=Change
        t.WeekHigh52=WeekHigh52
        t.WeekLow52=WeekLow52
        t.LastTradedPrice=LastTradedPrice
        t.High=High
        t.Low=Low
        t.Open=Open
        t.TradedValInCrs=TradedValInCrs
        t.TradedValInLacs=TradedValInLacs
        t.save()

def deleteFromDb(Ticker):
     try:
        models.stock.objects.filter(Symbol=Ticker).delete()
        return True
     except models.stock.DoesNotExist:
        return False


@login_required
def dashboard(request):
    print("\n\n return csv", dataparse.csv_return())
    source = dataparse.csv_return()
    for data in source:
            print("hello")
            addToDb(data["Symbol"], float(data["30 Days % Change"].replace(',', '')), float(data["365 Days % Change"].replace(',', '')), float(data ["%Change"].replace(',', '')), float(data["Change"].replace(',', '')), float(data["52 Week High"].replace(',', '')), float(data["52 Week Low"].replace(',', '')), float(data["Last Traded Price"].replace(',', '')), float(data["High"].replace(',', '')), float(data["Low"].replace(',', '')), float(data["Open"].replace(',', '')), float(data["Traded Value(crs)"].replace(',', '')),float(data ["Traded Volume(lacs)"].replace(',', '')))       
    return render(request, "dashboard.html",{"json": dataparse.dataparse()})
