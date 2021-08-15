**Spotify Playlist Creater**
This is a application that creates a playlist on Spotify of the one of the following per app run:
1. **Global Hot 100 Song List**
2. **Top 15 Anime Intros**
3. **Bollywood Top 20** 
The three .py files appart from main.py are the specific files for adding one of the above.
For running this application, user must have a Spotify account. Then follow the given steps:
1. Log in to https://developer.spotify.com/dashboard/login
2. From 'Create An App' button, create an app.
3. Open your app overview.
4. Through User Settings, create a "Redirect URI"
5. Enter Client ID, Client Secret, Redirect URI in data.csv
6. Now the app is ready to run.

This app runs through web scrapping **https://www.billboard.com/charts/hot-100** , **https://bestoftheyear.in/music/hindi/** , **https://www.ranker.com/list/best-anime-intros-and-opening-themes/lisa-waugh**
Please note, **this app is only for personal use. Any commercial use could lead to legal actions.**
