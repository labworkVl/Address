from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.views import APIView

from main.models import *
from main.serializers import *
from rest_framework.response import Response
from django.http import Http404


class StreetsList(APIView):

    def get(self, request):
        streets = Street.objects.all()
        ser = XstreetSerializer(streets, many=True)
        return Response(ser.data)


class StreetDetail(APIView):

    def get_object(self, pk):
        try:
            return Street.objects.get(pk=pk)
        except Street.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        streets = self.get_object(pk)
        ser = XstreetSerializer(streets)
        return Response(ser.data)


class DomaList(APIView):

    def get(self, request):
        doma = Dom.objects.all()
        ser = XdomSerializer(doma, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = XdomSerializer(data=request.data)
        print(ser.is_valid())
        return Response(ser.errors)


class DomaListStreet(APIView):

    def post(self, request, ds):
        doma = Dom.objects.filter(dom_street=ds)
        ser = XdomSerializer(doma, many=True)
        return Response(ser.data)

# ------------------------------------------------------- #
# ------------------------------------------------------- #
# ------------------------------------------------------- #
# ------------------------------------------------------- #
class StreetListMix(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Street.objects.all()
    serializer_class = XstreetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StreetList(APIView):
    def get(self, request, format='json'):
        if request.is_ajax():
            print(request.is_ajax())
            streets = Street.objects.all()
            ser = XstreetSerializer(streets, many=True)
            return Response(ser.data)
        else:
            return Response({})

    def post(self, request, format=None):
        streets = XstreetSerializer(data=request.data)
        if streets.is_valid():
            streets.save()
            return Response(streets.data,status=status.HTTP_201_CREATED)
        else:
            return Response(streets.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def streets_all(request):
    if request.method == "GET":
        serializer = XstreetSerializer(Street.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = XstreetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


