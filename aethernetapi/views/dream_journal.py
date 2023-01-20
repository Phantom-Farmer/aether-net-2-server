from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from aethernetapi.models import Dream_Journal, User, Sleep_Card

class DreamJournalView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single dream journal
        Returns:
            Response -- JSON serialized dream journal
        """
        dream_journal = Dream_Journal.objects.get(pk=pk)
        serializer = DreamJournalSerializer(dream_journal)
        return Response(serializer.data)


    def list(self, request):
        """"Handle GET requests to handle all dream journals"""
        dream_journals = Dream_Journal.objects.all()
        serializer = DreamJournalSerializer(dream_journals, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized dream journal
        """
        author = User.objects.get(pk=request.data["author"])
        sleep_card_id= Sleep_Card.objects.get(pk=request.data["sleep_card_id"])

        dream_journal = Dream_Journal.objects.create(
            author=author,
            sleep_card_id=sleep_card_id,
            dream=request.data["dream"],
            sleep_review=request.data["sleep_review"]
        )
        serializer = DreamJournalSerializer(dream_journal)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a dream journal
        Returns:
            Response -- Empty body with 204 status code
        """

        dream_journal = Dream_Journal.objects.get(pk=pk)

        author = User.objects.get(pk=request.data["author"])
        sleep_card_id = Sleep_Card.objects.get(pk=request.data["sleep_card_id"])

        dream_journal.author=author
        dream_journal.sleep_card_id=sleep_card_id
        dream_journal.dream=request.data["dream"]
        dream_journal.sleep_review=request.data["sleep_review"]
        dream_journal.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        dream_journal = Dream_Journal.objects.get(pk=pk)
        dream_journal.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class DreamJournalSerializer(serializers.ModelSerializer):
    """JSON serializer for dream journals
    """
    class Meta:
        model = Dream_Journal
        fields = ('id', 'author', 'sleep_card_id', 'dream', 'sleep_review')
        depth = 1
