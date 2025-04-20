from rest_framework import serializers
from .member import MemberSerializer


class MultiMemberSerializer(serializers.Serializer):
    team = MemberSerializer(many=True, required=False)
    applicants = MemberSerializer(many=True, required=True)