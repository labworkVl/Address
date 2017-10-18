from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from rest_framework.views import APIView
from main import apiView
# Create your views here.
from main.models import *
from main.serializers import StreetSerializer, XstreetSerializer
from ttmmpp.MsAccessDb import MsAccessConnector
import json
from django.forms.models import model_to_dict
from main import serializers

def read_otsaldk():
    kk = MsAccessConnector.exec_q('select * from adresa')
    for k in kk:
        yield k


xstr = lambda s: '' if s is None else s


def index(request):
    for d in read_otsaldk():
        if d[0] is not None:
            obj, created = Street.objects.get_or_create(name=str(d[0]))
            dobj, dcreated = Dom.objects.get_or_create(dom_street=obj, name="%s%s" % (int(d[1]), xstr(d[2])), num=int(d[1]), buk=xstr(d[2]))
            print("street - %s  --- dom - %s%s" % (d[0], d[1], xstr(d[2])))
    return render_to_response('index.html', {})


@csrf_exempt
def return_data(request):
    if request.is_ajax() and request.method == "POST":
        if request.POST['type'] == "streets":
            serializer = XstreetSerializer(Street.objects.all(), many=True)
            return JsonResponse(serializer.data, safe=False)
            #serializer = XstreetSerializer(Street.objects.all(), many=True)
            #return JsonResponse(serializer.data, safe=False)
        else:
            return HttpResponse("none")
    else:
        if request.method == 'GET':
            if request.GET['type'] == "1":
                serializer = StreetSerializer(Street.objects.all(), many=True)
                return JsonResponse(serializer.data, safe=False)
        else:
            return HttpResponse("noneG")


@csrf_exempt
def streets_list(request):
    if request.method == "GET":
        serializer = XstreetSerializer(Street.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        return HttpResponse("POST")

