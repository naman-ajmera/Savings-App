from django.db import models

from plan.models import Plan

# Create your models here.

class CustomerGoals(models.Model):
    planID = models.ForeignKey(Plan, on_delete=models.CASCADE)
    selectedAmount = models.DecimalField(decimal_places=2, max_digits=10)
    selectedTenure = models.IntegerField()
    startedDate = models.DateField(auto_now=True)
    depositedAmount = models.DecimalField(decimal_places=2, max_digits=10)
    benefitPercentage = models.DecimalField(decimal_places=2, max_digits=10)
    benefitType = models.CharField(max_length=100)