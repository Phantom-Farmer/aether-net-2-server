from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from aethernetapi.models import SC_Tag, Tag, Sleep_Card
from aethernetapi.views import TagSerializer


class SCTagView(ViewSet):
    """sleep tag view"""

    def retrieve(self, request, pk):
        try:
            sc_tag = SC_Tag.objects.get(pk=pk)
            serializer = SCTagSerializer(sc_tag)
            return Response(serializer.data)
        except SC_Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        def get_tags_for_sleep_card(sc_id):
            sleep_number = Sleep_Card.objects.get(id=sc_id)
            sc_tags = SC_Tag.objects.filter(sleep_number=sleep_number)
            return sc_tags

        sc_id = request.query_params.get('sleep_card', None)
        if sc_id is not None:
            sc_tags = get_tags_for_sleep_card(sc_id)
            serializer = SCTagSerializer(sc_tags, many=True)
            return Response(serializer.data)
        else:
            sc_tags = SC_Tag.objects.all()
            serializer = SCTagSerializer(sc_tags, many=True)
            return Response(serializer.data)

    def create(self, request):
        tag = Tag.objects.get(id=request.data["tag_id"])
        sleep_number = Sleep_Card.objects.get(pk=request.data["sleep_number_id"])

        sc_tag = SC_Tag.objects.create(
        sleep_number=sleep_number,
        tag=tag
        )
        serializer = SCTagSerializer(sc_tag)
        return Response(serializer.data)

    def update(self, request, pk):
        sc_tag = SC_Tag.objects.get(pk=pk)
        sc_tag.save()
  
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        sc_tag = SC_Tag.objects.get(pk=pk)
        sc_tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SCTagSerializer(serializers.ModelSerializer):
    sc_id = serializers.ReadOnlyField(source='sleep_card.id')
    tag_label = serializers.ReadOnlyField(source='tag.label')
    tag_id = serializers.ReadOnlyField(source='tag.id')
    class Meta:
        model = SC_Tag
        fields = ('id', 'sc_id', 'tag_label', 'tag_id')
