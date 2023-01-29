from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from aethernetapi.models import SC_Tag, Sleep_Card, Tag


class SCTagsView(ViewSet):
    """ SC_Tags View"""

    def retrieve(self, request, pk):
      try:
        sc_tag = SC_Tag.objects.get(pk=pk)
        serializer = SCTagSerializer(sc_tag)
        return Response(serializer.data)
      except SC_Tag.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
    def list(self, request):
      def get_tags_for_sc(sleep_number):
        sleep_number = Sleep_Card.objects.get(id=sleep_number)
        sc_tags = SC_Tag.objects.all(sleep_number=sleep_number)
        serializer = SCTagSerializer(sc_tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POSt operations
        Returns
            Response -- JSON serialized SC_Tag instance
        """
        sleep_number = Sleep_Card.objects.get(pk=request.data['sleep_number'])
        tag = Tag.objects.get(pk=request.data['tag'])

        sc_tag = SC_Tag.objects.create(
          sleep_number = sleep_number,
          tag = tag
        )

        serializer = SCTagSerializer(sc_tag)
        return Response(serializer.data)

    def update(self, request, pk):
        sc_tag = SC_Tag.objects.get(pk=pk)

        sleep_number = Sleep_Card.objects.get(pk=request.data["sleep_number"])
        tag = Tag.objects.get(pk=request.data["tag"])

        sc_tag.sleep_number = sleep_number
        sc_tag.tag = tag
        sc_tag.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        sc_tag = SC_Tag.objects.get(pk=pk)
        sc_tag.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SCTagSerializer(serializers.ModelSerializer):
    """JSON serializer for SC Tag"""

    class Meta:
        model = SC_Tag
        fields = ('id', 'sleep_number', 'tag')
        depth = 1
