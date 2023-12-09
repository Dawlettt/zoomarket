from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import News
from .serializers import NewsSerializer


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def newsList(request):
    if request.method == "GET":
        try:
            queryset = News.objects.all()
            serializer = NewsSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        try:
            serializer = NewsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Qátelik, qayta kiritiń"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE",'PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def newsDetail(request, id):
    try:
        device = News.objects.get(id=id)
    except News.DoesNotExist:
        return Response({"message": "Maǵlumat tabılmadı"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NewsSerializer(device, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'
        serializer = NewsSerializer(instance=device, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        device.delete()
        return Response({"message": "Maǵlumat óshirildi"}, status=status.HTTP_204_NO_CONTENT)
