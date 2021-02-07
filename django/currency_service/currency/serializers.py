from rest_framework import serializers


class CurrencySerializer(serializers.Serializer):
    id = serializers.CharField(required=True, max_length=3)
    value = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_id(self, value):
        return value.upper()


class CurrencyValueSerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=10, decimal_places=2)
