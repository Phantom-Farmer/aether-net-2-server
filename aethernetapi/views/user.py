from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from aethernetapi.models import User

class UserView(ViewSet):

    def retrieve(self, request, pk):

        try:

            user = User.objects.get(pk=pk)
            serializer = Userserializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):

        user = User.objects.create(
            uid=request.data['uid'],
        profile_image_url = request.data['profile_image_url'],
        email = request.data['email'],
        last_login = request.data['last_login'],
        )
        serializer = Userserializer(user)
        return Response(serializer.data)

    def update(self, request, pk):

        user = User.objects.get(pk=pk)

        uid=request.data['uid']
        profile_image_url = request.data['profile_image_url']
        email = request.data['email']
        last_login = request.data['last_login']
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uid', 'profile_image_url', 'email', 'last_login')
        depth = 1
