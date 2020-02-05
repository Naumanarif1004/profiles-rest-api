from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profile_api import serializers
from profile_api import models
from profile_api import permissions

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

class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self, request):
        a_viewset=[
        'User action(list, create, retrieve, Update, partial_update, delete)',
        'Automatically maps to URLs using Routers',
        'provides more functionality with less code',
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'hello {name}!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        return Response({'http_Method':'GET'})

    def update(self, request, pk=None):
        return Response({'http_Method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_Method':'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_Method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
