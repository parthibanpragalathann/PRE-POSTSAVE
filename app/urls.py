from .views import *
from django.urls import path

#application urls ...
urlpatterns = [
    path('credit/', CreditView.as_view(), name="Credit View"),                 #all the Credit details using GET and POST
    path('credit/<int:id>/', CreditModifyView.as_view(), name="Tasks Modify View"), #all the Credit details using PUT and DELETE
    path('loan/', LoanView.as_view(), name="Loan View"),  # all the Loan details using GET
    path('loan/<int:id>/', LoanDeleteView.as_view(), name="Loan Delete View"),
    # all the Loan details using DELETE
    path('debit/', DebitView.as_view(), name="Debit View"),  # all the Debit details using GET & POST
    path('debit/<int:id>/', DebitModifyView.as_view(), name="Debit Modify View"),
    # all the Debit using PUT & DELETE
    path('balance/', BalanceView.as_view(), name="balance View"),  # all the balance details using GET
    path('balance/<int:id>/', BalanceDeleteView.as_view(), name="balance Delete View"),
    # all the balance using DELETE

]