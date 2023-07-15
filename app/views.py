
from django.shortcuts import render,redirect,HttpResponse

from .models import blood
from .serializers import bloodserializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from rest_framework import status

# Create your views here.
# def list(request):
#     return HttpResponse("hello")




#This function is for get

@api_view(['GET','POST','UPDATE','DELETE']) 
def list(request):
    model=blood.objects.all()                       #Query out database
    converter=bloodserializer(model,many=True)      #serialize the data
    return Response(converter.data)



#detailed view of each item with id
@api_view(['get','put','post'])
def listdetails(request,pk):
    model=blood.objects.get(pk=pk)
    serializer=bloodserializer(model,many=False)
    return Response(serializer.data)
    
#This function is for add
#Adding data with our API (Django rest_framework is also API)

@api_view(['POST'])    #This view will allow only post method
def addlist(request):
    
    convert=bloodserializer(data=request.data)  #convert is a variable we are gonna pass in some data so data equals to request.data in case of modelform request.post because this is an API view we have access to request.data basically request.data sends us a JSON object and that's how we are gonna work with it to standardize we do validity if it's valid it will send the item back to database and save it
    if convert.is_valid():
        convert.save()    
    return Response(convert.data)


    


#This function is for delete

'''@api_view(['DELETE'])
def deleteuser(request,pk):
    var= blood.objects.get(id=pk)     #id=pk or pk=pk both can be done.
    var.delete()
    return Response("Record successfully deleted")  '''
    
@api_view(['DELETE'])
def deleteuser(request,id):             #(request,id) or (request,pk) also can be done but in url you must pass accordingly where pk is primary key
    var= blood.objects.get(pk=id)       #pk=id or id=id both can be done
    var.delete()
    return Response("Record successfully deleted")        


'''Note:(request,id) or (request,pk) anyway it can work from the Angular side'''








#This function is for update


'''@api_view(['post','put','get'])          #post or POST or Post anyways it can work
def updateuser(request,id):
    modela= blood.objects.get(id=id)      
    converter=bloodserializer(instance=modela, data=request.data)
    
    if converter.is_valid():
        converter.save()
    
    return Response(converter.data) '''


'''with the help of primary key or id we are gonna grab the particular item
first and throw that inside the modela variable and we are gonna get the object
that we want to update and data is gonna equal to request.data but just like the
form we are gonna set the instance  of creating a new item we are gonna set instance to 
and we are gonna update the instance of the item that's in the id so serializer 
instance is that modela we go ahead and check if it's valid and save that and change the
path in the URL'''


#This is a function for update

'''
@api_view(['PUT'])
def updateDoner(request, pk):
    data = request.data
    model = blood.objects.get(id=pk)
    serializer = bloodserializer(instance=model, data=data)

    if serializer.is_valid():
       serializer.save()
    return Response(serializer.data) '''
    

#cloned
'''@api_view(['PUT','PATCH'])
def update_info(request, pk):
    info_obj = blood.objects.get(pk=pk)
    serializer = bloodserializer(info_obj, data=request.data)
    #if serializer.is_valid():
        #serializer.save()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_200_OK  )
 
'''


'''
@api_view(['PUT','PATCH'])
def updatedoner(request, pk):
    info_obj = blood.objects.get(pk=pk)
    serializer = bloodserializer(info_obj, data=request.data)
    #if serializer.is_valid():
        #serializer.save()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_200_OK)'''
    
@api_view(['PUT'])
def updatedoner(request,pk):
    modela= blood.objects.get(id=pk)      
    converter=bloodserializer(instance=modela, data=request.data)
    
    if converter.is_valid():
        converter.save()
    
    return Response(converter.data)    
    
    


