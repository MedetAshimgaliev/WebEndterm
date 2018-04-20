from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import postapi
from .serializers import blogSerializer

@csrf_exempt
def post_list(request):
  if request.method == "GET":
    posts1 = postapi.objects.all()
    serializer = blogSerializer(posts1,many=True)
    return JsonResponse(serializer.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    serializer = blogSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def post_detail(request, post_id):
  
  try:
    post = postapi.objects.get(pk=post_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    serializer = blogSerializer(post)
    return JsonResponse(serializer.data) 
  elif request.method == "PUT":
    data = JSONParser().parse(request)
    serializer = blogSerializer(post, data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
  elif request.method == "DELETE":
    employee.delete()
    serializer = blogSerializer(post)
    return JsonResponse(serializer.data)