from rest_framework import serializers


class AttributeSerializer(serializers.Serializer):
    intelligence = serializers.IntegerField()
    strength = serializers.IntegerField()
    endurance = serializers.IntegerField()
    spicyFoodTolerance = serializers.IntegerField()


class MemberSerializer(serializers.Serializer):
    name = serializers.CharField()
    attributes = AttributeSerializer()
