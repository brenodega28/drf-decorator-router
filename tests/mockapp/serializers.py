from rest_framework import serializers

from . import models


class MockProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MockProduct
        exclude = []


class MockStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MockStore
        exclude = []