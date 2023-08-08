from rest_framework import serializers
from .models import Gigs

class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gigs
        fields = '__all__'