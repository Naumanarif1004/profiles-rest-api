from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test the API View """
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP methods as Fuction(get, post, put, patch, delete)',
        'is similar to traditinal django view',
        'gives you the most control over your application logic',
        'is mapped manually to URLs',
        ]
        return Response(
        {'message':'hello!','an_apiview':an_apiview}
        )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})
