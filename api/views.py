from functools import partial
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from numpy import delete
from rest_framework.views import APIView
from .serialzer import *
from .models import record
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
# Create your views here.


class studentview(APIView):

    def get(self,request,id=None,format=None):
        if id is not None:
            try:
                s=record.objects.get(id=id)
                s=firstserializer(s)
            except:
                msg={"msg":"id does not exists"}
                return Response(msg)    
        else:
            s=record.objects.all()
            s=firstserializer(s,many=True)
        
        return Response(s.data)


    def post(self,request,format=None):
        
        s=firstserializer(data=request.data)
        print(s)
        if s.is_valid():
            s.save()
            msg={'msg':'data saved into db'}
            return Response(msg)
        return Response(s.error_messages)    


    def put(self,request,id=None,format=None):

        if id is not None:
            print(id)
            obj=record.objects.get(id=id)
            s=firstserializer(obj,data=request.data)
            if s.is_valid():
                s.save()
                msg={'msg':'data updated'}
                return Response(msg)
        else:
            id=request.data['id']
            obj=record.objects.get(id=id)
            s=firstserializer(obj,data=request.data)
            if s.is_valid():
                s.save()
                msg={'msg':'data updated'}
                return Response(msg)
        return Response(s.error_messages)    

    def patch(self,request,id=None,format=None):
        if id is not None:
            print(id)
            obj=record.objects.get(id=id)
            s=firstserializer(obj,data=request.data)
            if s.is_valid():
                s.save()
                msg={'msg':'data updated'}
                return Response(msg)
        else:        
            id=request.data['id']
            obj=record.objects.get(id=id)
            s=firstserializer(obj,data=request.data,partial=True)
            if s.is_valid():
                s.save()
                msg={'msg':'data updated'}
                return Response(msg)
            return Response(s.error_messages)    
    
    def delete(self,request,id):
        obj=record.objects.get(id=id)
        print(obj)
        obj.delete()
        msg={'msg':'data delete'}
        return Response(msg)
        