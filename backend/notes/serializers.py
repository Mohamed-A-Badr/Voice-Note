from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = (
            "title",
            "url",
            "content",
            "created_at",
        )
        extra_kwargs = {
            "created_at": {"read_only": True},
            "url": {"read_only": True},
        }

    def get_url(self, obj):
        return obj.get_absolute_url()

    def create(self, validated_data):
        return super().create(validated_data)


class TextToSpeechSerializer(serializers.Serializer):
    text = serializers.CharField(
        style={"base_template": "textarea.html"}, required=True, write_only=True
    )
