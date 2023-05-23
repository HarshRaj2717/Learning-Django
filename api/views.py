from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer

# Create your views here.


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@permission_classes([AllowAny,])
def hello(request):
    x = {'name': 'Harsh', 'marks': [99, 98, 89,
                                    {100: 200}, [1, 2, 3, 4, 6, 7, 8, 900]]}
    return Response(x)


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(item_location=location)
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
