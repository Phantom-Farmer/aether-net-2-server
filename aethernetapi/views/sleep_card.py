import datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from aethernetapi.models import Sleep_Card, User

class SleepCardView(ViewSet):

    def retrieve(self, request, pk):

        sleep_card = Sleep_Card.objects.get(pk=pk)
        serializer = SleepCardSerializer(sleep_card)
        return Response(serializer.data)

    def list(self, request):

        sleep_cards = Sleep_Card.objects.all()
        uid_query = request.query_params.get('uid', None)
        if uid_query is not None:
            sleep_cards = sleep_cards.filter(user=uid_query)
        serializer = SleepCardSerializer(sleep_cards, many = True)
        return Response(serializer.data)

    def create(self, request):

        author = User.objects.get(uid=request.data["user"])

        sleep_card = Sleep_Card.objects.create(
            time_stamp = datetime.date.today(),
            mind = request.data["mind"],
            body = request.data["body"],
            meditation = request.data["meditation"],
            favorite = request.data["favorite"],
            author = author
        )
        serializer = SleepCardSerializer(sleep_card)
        return Response(serializer.data)

    def update(self, request, pk):

        sleep_card = Sleep_Card.objects.get(pk=pk)

        sleep_card.time_stamp = datetime.date.today()
        sleep_card.mind = request.data["mind"]
        sleep_card.body = request.data["body"]
        sleep_card.meditation = request.data["meditation"]
        sleep_card.favorite = request.data["favorite"]
        sleep_card.author = request.data["author"]
        sleep_card.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        sleep_card = Sleep_Card.objects.get(pk=pk)
        sleep_card.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SleepCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sleep_Card
        fields = ('id', 'time_stamp', 'mind', 'body', 'meditation', 'favorite', 'author')
        depth = 1
