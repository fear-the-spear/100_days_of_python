import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

from PRIVATE.vars import *

REDIRECT_URI = "https://example.com"

chosen_date = input(
    "To which date would you like to travel? Use this format -> YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{chosen_date}"

response = requests.get(url=URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")

song_titles = soup.select(selector="li li h3")
songs = [songs.getText().strip() for songs in song_titles]


scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, username="dakotabb1", show_dialog=True, cache_path="token.txt"))

################################################################################

user_id = sp.current_user()["id"]
song_uris = []
for n in range(len(songs)):
    data = sp.search(
        q=f"track:{songs[n]} year:{chosen_date.split('-')[0]}", type="track")
    try:
        uri = data["tracks"]["items"][0]["uri"]
    except IndexError:
        uri = ""
    else:
        song_uris.append(uri)

new_playlist = sp.user_playlist_create(
    user=user_id, name=f"{chosen_date} Billboard Hot 100", public=False, description="A playlist generated with Python :)")
playlist_id = new_playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
