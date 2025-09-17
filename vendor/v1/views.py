from rest_framework.decorators import  api_view
from ..models import Vendor
from .serializers import VendorSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,HTTP_204_NO_CONTENT

@api_view(['GET', 'POST'])
def get_list_create_vendor(request):
    if request.method=='GET':
        vendors= Vendor.objects.all()
        serialized=VendorSerializer(vendors, many=True)
        return Response(serialized.data,status=HTTP_200_OK)
    if request.method=='POST':
        serializer=VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)
        Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH','DELETE'])
def get_update_delete(request,pk):
    try:
        vendor=Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=VendorSerializer(vendor)
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method=='PATCH':
        serializer=VendorSerializer(vendor,data=request.data, partial=True)
        return Response(serializer.data,status=HTTP_200_OK)
    if request.method=='DELETE':
        vendor.delete()
        return Response(status=HTTP_204_NO_CONTENT)



