from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homePageView(requesr):
    return HttpResponse('Hello,Mouad !')
