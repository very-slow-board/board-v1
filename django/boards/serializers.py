from rest_framework import serializers

from .models import Board


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'pk',
            'title',
        )


class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'pk',
            'title',
            'content',
        )
