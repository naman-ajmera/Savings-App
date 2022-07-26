from rest_framework import  serializers
from .models import CustomerGoals

class CustomerGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGoals
        fields = '__all__'