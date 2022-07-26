from django.db import models

# Create your models here.

class Amount(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.amount)

class Tenure(models.Model):
    tenure = models.IntegerField()

    def __str__(self):
        return str(self.tenure)

class Plan(models.Model):
    planName = models.CharField(max_length=100)
    amountOptions = models.ManyToManyField(Amount)
    tenureOptions = models.ManyToManyField(Tenure)
    benefitPercentage = models.IntegerField()
    benefitType = models.CharField(max_length=100)
    #promotion = models.CharField(max_length=100)
    promotionType = models.CharField(max_length=100, blank=True)
    promotionStartDate = models.DateField(blank=True, null=True)
    promotionEndDate = models.DateField(blank=True, null=True)
    promotionCountByUser = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now=True)
    isPromotionActive = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)