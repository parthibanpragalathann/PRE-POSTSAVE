# DRF django signals pre save and post save with postgresql

````doctest
   Create and Connect Database (postges)
   Create and activate Virtual environment
````

### Install packages and Create projects and apps.
````python 
    pip install django
    pip install djangorestframework
    pip install psycopg2
    django-admin satrtproject api .
    django-admin satrtapp app
````

## pre save 
````doctest 
Create and use two models CreditAmount and LoanAmount
for pre save in django signals. 
````
````python
class CreditAmount(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    def __str__(self):
        return self.name

class LoanAmount(models.Model):
    loan_details = models.TextField(default='{}')

````

## post save
````doctest 
Create and use two models DebitAmount and BalanceAmount
for post save in django signals. 
````
````python

class DebitAmount(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    def __str__(self):
        return self.name

class BalanceAmount(models.Model):
    debit_person = models.ForeignKey(DebitAmount, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)

````

## Django signals

````doctest
1.)signal dispatcher” which helps decoupled applications get 
notified when actions occur elsewhere in the not framework
2.)Only use signals to avoid introducing circular dependencies. 
PRE SAVE:
    Actions to take before the model's save is called.
    Emit a pre-save signal. Pre-process the data.

POST SAVE:
    Actions to take after the model's save is called.
    Emit a post-save signal. Post-process the data.
````
````python
@receiver(pre_save, sender=CreditAmount)
def credit_loan(sender, instance, **kwargs):
    print("Pre save", instance.name, instance.amount)
    credit_data = {'loan user': instance.name, 'loan amount': instance.amount}
    LoanAmount.objects.create(loan_details=json.dumps(credit_data))

@receiver(post_save, sender=DebitAmount)
def debit_balance(sender, instance, **kwargs):
    print("Post save", instance.name, instance.amount)
    BalanceAmount.objects.create(debit_person=instance, date=datetime.datetime.now())
````
## APPLICATIONS URLS
````python
GET, POST

    http://127.0.0.1:8000/root/credit/
    http://127.0.0.1:8000/root/debit/

GET PUT PATCH DELETE

    http://127.0.0.1:8000/root/credit/id/
    http://127.0.0.1:8000/root/debit/id/

GET

    http://127.0.0.1:8000/root/loan/
    http://127.0.0.1:8000/root/balance/

GET DELETE

    http://127.0.0.1:8000/root/loan/id/
    http://127.0.0.1:8000/root/balance/id/
````