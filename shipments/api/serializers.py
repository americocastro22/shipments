from rest_framework import serializers

from .models import Shipment, StatusChoices


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

    def create(self, validated_data):
        if validated_data.get('status', StatusChoices.CREATED) != StatusChoices.CREATED:
            raise serializers.ValidationError({"status": [f'{validated_data["status"]} is not valid on create']})
        if validated_data.get('complete', False):
            raise serializers.ValidationError({"complete": ['\"true\" is not valid on create']})
        return Shipment.objects.create(**validated_data)
