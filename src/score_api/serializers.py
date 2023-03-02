from rest_framework.serializers import ModelSerializer
from .models import Game, Score

class GameSerializer(ModelSerializer):

    class Meta:
        model = Game
        fields = ['id', 'name']
    


class ScoreSerializer(ModelSerializer):

    class Meta:
        model = Score
        fields = ['id', 'game', 'player', 'score']


