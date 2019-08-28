from django.db import models
from user.models import user
# Create your models here.

class stock(models.Model):
    Symbol = models.CharField(max_length=30)
    PercentChange30 = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    PercentChange365 = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    PercentChange = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    Change = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    WeekHigh52 = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    WeekLow52 = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    LastTradedPrice = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    High = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    Low = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    Open = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    TradedValInCrs = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    TradedVolInLacs = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    email = models.ForeignKey(
        user,
         on_delete=models.CASCADE,
         null=True
    )




