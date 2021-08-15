import tkinter

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime as dt
import pandas

file = pandas.read_csv("data.csv")
name = list(file["name"])
data = list(file["data"])
CLIENT_ID = data[name.index("client_id")]
CLIENT_SECRET = data[name.index("client_secret")]
REDIRECT_URI = data[name.index("redirect_uri")]


def get_titles():
    response = requests.get(url="https://www.billboard.com/charts/hot-100")
    response.raise_for_status()
    html_data = response.text

    soup = BeautifulSoup(html_data, "html.parser")
    data = soup.find_all(name="span", class_="chart-element__information__song", limit=100)

    title_list = []
    for one_set in data:
        title = one_set.getText()
        title_list.append(title)
    print("Song Titles Successfully Retrieved")
    print("Authorizing Spotify Account...")
    create_playlist(title_list, "Global Hot 100")
    return


def create_playlist(title_list, playlist_name):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                  client_secret=CLIENT_SECRET,
                                  redirect_uri=REDIRECT_URI, scope="playlist-modify-private",
                                  show_dialog=True, cache_path="token.txt")
    )
    user_id = sp.current_user()["id"]
    print("Spotify Account Successfully Authorized")
    print("Retrieving Song URIs...")

    today = dt.datetime.now()
    year = today.year
    songs_uri = []
    for title in title_list:
        result = sp.search(q=f"track:{title} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            songs_uri.append(uri)
        except IndexError:
            print(f"Song with name: '{title}' not present on Spotify. Passed")
    print("Song URIs Successfully Retrieved")
    print("Creating Playlist...")

    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    playlist_id = playlist["id"]
    print("Playlist Successfully Created")
    print("Adding Songs To Playlist...")

    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=songs_uri)
    print("Songs Added To Playlist")
    print(f"Playlist named {playlist_name} with {len(songs_uri)} tracks successfully added")
    return
