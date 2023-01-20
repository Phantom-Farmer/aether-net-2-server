from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from aethernetapi.models import Sleep_Card, Tag, SC_Tag

class SCTagsView(ViewSet):
    """ SC_Tags View"""

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized SleepCard instance
        """
        tag = Tag.objects.get(pk=request.data['tag_id'])
        sleep_card = Sleep_Card.objects.get(pk=request.data['sleepCard_id'])

        sc_tag = SC_Tag.objects.create(
          tag = tag,
          sleep_card = sleep_card
        )

        serializer = SCTagSerializer(sc_tag)
        return Response(serializer.data)

    def destroy(self, request, pk):
        sc_tag = SC_Tag.objects.get(pk=pk)
        sc_tag.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SCTagSerializer(serializers.ModelSerializer):
    """JSON serializer for SC Tag"""

    class Meta:
        model = SC_Tag
        fields = ('id', 'tag', 'sleep_card')
        depth = 1
