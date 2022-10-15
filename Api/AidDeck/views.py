from django.shortcuts import render
from .models import BankDetails, BankWallet, FundApply, Missionary
from .serializers import BankDetailsSerializer,BankWalletSerializer,FundApplySerializer,UserSerializer,MissionarySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

@api_view(["GET","POST"])
def bank(request,format=None):
    if request.method=='GET':
        bank=BankDetails.objects.all()
        serializer=BankDetailsSerializer(bank,many=True)

        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=BankDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(["GET","POST"])
def wallet(request,format=None):
    if request.method=='GET':
        bank=BankWallet.objects.all()
        serializer=BankWalletSerializer(bank,many=True)

        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=BankWalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(["GET","POST"])
def fund(request,format=None):
    if request.method=='GET':
        bank=FundApply.objects.all()
        serializer=FundApplySerializer(bank,many=True)

        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=FundApplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(["GET","POST"])
def user(request,format=None):
    if request.method=='GET':
        bank=User.objects.all()
        serializer=UserSerializer(bank,many=True)

        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(["GET","POST"])
def mission(request,format=None):
    if request.method=='GET':
        bank=Missionary.objects.all()
        serializer=MissionarySerializer(bank,many=True)

        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=MissionarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)