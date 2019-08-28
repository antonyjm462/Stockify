from dashboard.models import stock

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