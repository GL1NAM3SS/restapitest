from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Topic
from .serializers import TopicSerializer

class TopicView(APIView):
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response({'topic': serializer.data})

    def post(self, request):
        topic = request.data

        serializer = TopicSerializer(data=topic)
        if serializer.is_valid(raise_exception=True):
            topic_saved = serializer.save()
            return Response({'success': 'Topic {} created successfully'.format(topic_saved.title)})

    def put(self, request, pk):
       # saved_topic = get_object_or_404(Topic.objects.all())
        saved_topic = get_object_or_404(Topic.objects.filter(id=pk))
        data = request.data.get('topic')
        serializer = TopicSerializer(instance=saved_topic, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            topic_saved = serializer.save()
        return Response({
            "success": "Topic '{}' updated successfully".format(topic_saved.title)
        })

    def delete(self, request, pk):
        topic = get_object_or_404(Topic.objects.all(), pk=pk)
        topic.delete()
        return Response({
            "message": "Topic with id `{}` has been deleted.".format(pk)
        }, status=204)