from django.db import models
from user.models import user
# Create your models here.

class stock(models.Model):
    Symbol = models.CharField(max_length=30)
    PercentChange30 = models.DecimalField(decimal_places=2, max_digits=6)
    PercentChange365 = models.DecimalField(decimal_places=2, max_digits=6)
    PercentChange = models.DecimalField(decimal_places=2, max_digits=6)
    Change = models.DecimalField(decimal_places=2, max_digits=6)
    WeekHigh52 = models.DecimalField(decimal_places=2, max_digits=6)
    WeekLow52 = models.DecimalField(decimal_places=2, max_digits=6)
    LastTradedPrice = models.DecimalField(decimal_places=2, max_digits=6)
    High = models.DecimalField(decimal_places=2, max_digits=6)
    Low = models.DecimalField(decimal_places=2, max_digits=6)
    Open = models.DecimalField(decimal_places=2, max_digits=6)
    TradedValInCrs = models.DecimalField(decimal_places=2, max_digits=6)
    TradedVolInLacs = models.DecimalField(decimal_places=2, max_digits=6)
    email = models.ForeignKey(
        user,
         on_delete=models.CASCADE
    )

def addToDb(Ticker, PercentChange30, PercentChange365, PercentChange, Change, WeekHigh52, WeekLow52, LastTradedPrice, High, Low, Open, TradedValInCrs, TradedValInLacs):
    "Adds/Updates a single set of stock details to the database"
    try:
        t = stock.objects.get(Symbol=Ticker)
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

    except stock.DoesNotExist:
        t=stock()
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
        stock.objects.filter(Symbol=Ticker).delete()
        return True
     except stock.DoesNotExist:
        return False


