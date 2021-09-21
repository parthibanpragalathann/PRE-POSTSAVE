from rest_framework import serializers
from .models import *


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditAmount
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAmount
        fields = '__all__'

class DebitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitAmount
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceAmount
        fields = '__all__'