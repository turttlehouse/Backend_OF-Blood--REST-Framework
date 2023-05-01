from rest_framework import  serializers
from .models import blood


#we want to serialize a model here so ModelSerializer but we can serialize any form of data.
class bloodserializer(serializers.ModelSerializer): #class name can be userdefined but I am following the trend model name followed by serializer
    class Meta:
        model= blood
        fields='__all__'  #fields that we want to serialize