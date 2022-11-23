from django.shortcuts import render
from .models import *
from django.views.generic.base import View
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse , JsonResponse
# Create your views here.
class home(View):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        # json_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data , content_type='application/json')
        return JsonResponse(serializer.data,safe=False)


