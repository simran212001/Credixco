
import json
from re import T
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from Credicxo.serializers import StudentSerializer
# Create your views here.
def Student_details(request,pk):
    # converting complex data to python native data
    # stu = Student.objects.get(id = 3)
    stu = Student.objects.get(id = pk)
    Serializer = StudentSerializer(stu)
    # converting python data to json data  import json renderer
    # json_data = JSONRenderer().render(Serializer.data)

    # return HttpResponse(json_data , content_type ='application/json')
    
    return JsonResponse(Serializer.data ,safe= False )



def Student_list(request):
    # converting complex data to python native data
    # stu = Student.objects.get(id = 3)
    stu = Student.objects.all()
    Serializer = StudentSerializer(stu , many = True)
    # converting python data to json data  import json renderer
    # json_data = JSONRenderer().render(Serializer.data)

    # return HttpResponse(json_data , content_type ='application/json')

    return JsonResponse(Serializer.data,safe=False )


