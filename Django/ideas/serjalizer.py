from .models import Idea, Vote
from res import serializers

class IdeaSerializer(serializers.HiperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'title', 'descripton', 'youtube_url', 'status']



class VoteSerializer(serializers.HiperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ['idea', 'reason']