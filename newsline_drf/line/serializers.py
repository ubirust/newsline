from rest_framework import serializers
from .models import Note, Achievement, Advertisement, Event


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_content_object(self, obj):
        if obj.event_type == 'note':
            return NoteSerializer(obj.content_object).data
        elif obj.event_type == 'achievement':
            return AchievementSerializer(obj.content_object).data
        elif obj.event_type == 'advertisement':
            return AdvertisementSerializer(obj.content_object).data
        else:
            raise Exception('Unknown event type')