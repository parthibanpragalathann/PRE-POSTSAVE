import datetime
from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
# from django.template.defaultfilters import slugify
import json

class CreditAmount(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    def __str__(self):
        return self.name

class LoanAmount(models.Model):
    loan_details = models.TextField(default='{}')

class DebitAmount(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    def __str__(self):
        return self.name

class BalanceAmount(models.Model):
    debit_person = models.ForeignKey(DebitAmount, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)

@receiver(pre_save, sender=CreditAmount)
def credit_loan(sender, instance, **kwargs):
    print("Pre save", instance.name, instance.amount)
    credit_data = {'loan user': instance.name, 'loan amount': instance.amount}
    LoanAmount.objects.create(loan_details=json.dumps(credit_data))

@receiver(post_save, sender=DebitAmount)
def debit_balance(sender, instance, **kwargs):
    print("Post save", instance.name, instance.amount)
    BalanceAmount.objects.create(debit_person=instance, date=datetime.datetime.now())
