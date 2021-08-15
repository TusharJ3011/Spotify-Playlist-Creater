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
    response = requests.get(url="https://www.ranker.com/list/best-anime-intros-and-opening-themes/lisa-waugh")
    response.raise_for_status()
    html_data = response.text

    soup = BeautifulSoup(html_data, "html.parser")
    data = soup.find_all(name="a", class_="gridItem_name__wCyGi", limit=15)

    title_list = []
    for one_set in data:
        title = one_set.getText()
        title = title.split(" - ")
        part1 = title[0].split(" Opening")[0]
        part2 = title[1]
        title = f"{part2}"
        title_list.append(title)
    print("Song Titles Successfully Retrieved")
    print("Authorizing Spotify Account...")
    create_playlist(title_list, "15 Best Anime Intros")
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
            data_split_1 = result["tracks"]["items"]
            index = 0
            for i in range(0, len(data_split_1)):
                index = i
                name = data_split_1[i]["artists"][0]["name"]
                if name == "Otaku":
                    break
            if name != "Otaku":
                a = 2 / 0
                pass
            uri = data_split_1[index]["uri"]
            songs_uri.append(uri)
        except (IndexError, ZeroDivisionError):
            print(f"Song with name: '{title}' not present on Spotify. Passed")
    print("Song URIs Successfully Retrieved")
    print("Creating Playlist...")

    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    playlist = playlist["id"]
    print("Playlist Successfully Created")
    print("Adding Songs To Playlist...")

    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist, tracks=songs_uri)
    print("Songs Added To Playlist")
    print(f"Playlist named {playlist_name} with {len(songs_uri)} tracks successfully added")
    return
