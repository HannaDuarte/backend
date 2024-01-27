from rest_framework import permissions, viewsets

from .serializers import ListSerializer, ItemSerializer
from .models import List, Item

class ListViewSet(viewsets.ModelViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]

class ItemViewSet(viewsets.ModelViewSet):
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

