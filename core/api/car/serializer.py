from rest_framework import serializers

from core.models import Car


class CarSerializer(serializers.ModelSerializer):
    """
    This serializer is for Car API. Here we can add any description.
    """
    class Meta:
        """
        This is meta class
        """
        model = Car
        fields = '__all__'
