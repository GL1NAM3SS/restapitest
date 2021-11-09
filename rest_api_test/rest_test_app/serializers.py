from rest_framework import serializers
from .models import Topic
class TopicSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=500)

    class Meta:
        model = Topic
        fields = [
            'title', 'text'
        ]

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('text', instance.description)

        instance.save()
        return instance
