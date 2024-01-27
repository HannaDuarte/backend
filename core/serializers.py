from .models import List, Item
from django.contrib.auth.models import Group, User
from rest_framework import serializers


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'owner', 'url']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ['name']


