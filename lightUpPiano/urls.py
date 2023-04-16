from django.urls import path
from .views import play_music, display_songs

urlpatterns = [
    path('music/play', play_music, name='play_music'),
    path('music/display', display_songs, name='display_songs')
]
