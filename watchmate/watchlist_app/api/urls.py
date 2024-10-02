from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import  WatchlistDetailAV, WatchListAV, StreamPlatformAV, StreamPlatformDetailAV


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>',  WatchlistDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path ('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream'),
]

