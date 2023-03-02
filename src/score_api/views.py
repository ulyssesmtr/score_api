from rest_framework.views import APIView
from .models import Game, Score
from .serializers import GameSerializer, ScoreSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class Games(APIView):
    """
    List all games, or create a new one.
    """
    def get(self, request):
        games = Game.objects.all()
        name = request.query_params.get('name')
        if name:
            games = games.filter(name__icontains=name)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameDetail(APIView):
    """
    Retrieves, updates and deletes Games instances.
    """

    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def put(self, request, pk):
        game = self.get_object(pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        game = self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 
class Scores(APIView):
    """
    List all scores, or create a new one.
    """
    def get(self, request):
        scores = Score.objects.order_by('-score')[:10]
        id = request.query_params.get('id')
        if id:
            range = request.query_params.get('range')
            if range:
                try:
                    score = Score.objects.get(pk=id)
                except Score.DoesNotExist:
                    raise Http404
                try:
                    upper_value = score.score + float(range)
                    lower_value = score.score - float(range)
                    scores = Score.objects.filter(score__gte = lower_value, score__lte=upper_value).order_by('-score')
                except Exception as e:
                    return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScoreDetail(APIView):
    """
    Retrieves, updates and deletes Games instances.
    """

    def get_object(self, pk):
        try:
            return Score.objects.get(pk=pk)
        except Score.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        score = self.get_object(pk)
        serializer = ScoreSerializer(score)
        return Response(serializer.data)

    def put(self, request, pk):
        score = self.get_object(pk)
        serializer = ScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        score = self.get_object(pk)
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)