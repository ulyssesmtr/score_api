from django.contrib import admin
from django.urls import path, include
from score_api import views




urlpatterns = [
    path('games/', views.Games.as_view(), name='games'),
    path('game-detail/<int:pk>', views.GameDetail.as_view(), name='game-detail'),
    path('scores/', views.Scores.as_view(), name='scores'),
    path('score-detail/<int:pk>', views.ScoreDetail.as_view(), name='score-detail'),
    ]   