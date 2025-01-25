from rest_framework import serializers

from CRUD.models import Chicken

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chicken
        fields='__all__'