from django.shortcuts import render
from django.http import JsonResponse
from .models import apidata
# Create your views here.

def js(request):
	data = list(apidata.objects.values())

	print(data)
	return JsonResponse(data,safe=False)
