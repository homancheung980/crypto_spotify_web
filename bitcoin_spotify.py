import spotipy
import json
import random
import base64
import urllib.request  # For accessing API
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

# Load crypto API base URL
with open("btc_api.txt", "r") as crypto_file:
    crypto_key = crypto_file.read().strip()

# Load Spotify API keys
with open("spotifykeys.json", "r") as spotify_file:
    tokens = json.load(spotify_file)

my_client_id = tokens["client_id"]
my_client_secret = tokens["client_secret"]
redirectURI = tokens["redirect"]
username = tokens["username"]

# Define scope and authenticate with Spotify
scope = "user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public"
token = util.prompt_for_user_token(
    username, scope, client_id=my_client_id, client_secret=my_client_secret, redirect_uri=redirectURI
)

# Create Spotify object
sp = spotipy.Spotify(auth=token)

# Function to get a crypto playlist
def get_btcplaylist(crypto):
    # API URL
    url = f"https://api.coinlore.net/api/ticker/?id={crypto}"

    # Fetch data from crypto API
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        crypto_json = json.loads(response.read())

        # Check if the response contains data
        if not crypto_json or "percent_change_24h" not in crypto_json[0]:
            raise ValueError("Invalid data from crypto API")

        # Get the percent change in crypto value
        crypto_value_change = float(crypto_json[0]["percent_change_24h"])

    except (urllib.error.URLError, json.JSONDecodeError, ValueError) as e:
        # Handle errors (e.g., connection issues, empty data, or invalid data)
        print(f"Error fetching or parsing crypto data: {e}")
        return None

    # Set keyword for song search
    keyword = ["lost", "alone", "sad"] if crypto_value_change < 0 else ["winning", "money", "bread"]
    keyword_query = " OR ".join(keyword)

    # Collect track IDs from Spotify
    track_ids = []
    offsets = [random.randint(0, 1000) for _ in range(4)]  # Generate 4 random offsets

    for offset in offsets:
        track_results = sp.search(q=keyword_query, type="track", limit=50, offset=offset)
        for track in track_results["tracks"]["items"]:
            track_ids.append(track["id"])

    # Filter songs based on audio features
    all_filtered_songs = []
    batch_size = 50  # Spotify API processes up to 50 tracks at once

    for i in range(0, len(track_ids), batch_size):
        batch_ids = track_ids[i:i + batch_size]
        ind_audio_features = sp.audio_features(batch_ids)

        if crypto_value_change < 0.0:
            # Filter for negative change (sad/slow songs)
            filtered_songs = [
                track for track, features in zip(batch_ids, ind_audio_features)
                if features
                and features["mode"] == 0  # Minor key
                and features["danceability"] <= 0.3
                and (features["tempo"] <= 100 or features["energy"] <= 0.5 or features["valence"] <= 0.7)
            ]
        else:
            # Filter for positive change (happy/upbeat songs)
            filtered_songs = [
                track for track, features in zip(batch_ids, ind_audio_features)
                if features
                and features["mode"] == 1  # Major key
                and features["danceability"] >= 0.6
                and (features["tempo"] >= 110 or features["energy"] >= 0.7 or features["valence"] >= 0.4)
            ]

        all_filtered_songs.extend(filtered_songs)

    # Limit to the top 10 songs
    all_filtered_songs = all_filtered_songs[:10]

    # Collect song URIs
    song_uris = [f"spotify:track:{song}" for song in all_filtered_songs]

    #Make title change according to inputs
    crypto_name = ""
    if crypto == "90":
    	crypto_name = "BTC"
    elif crypto == "80":
    	crypto_name = "ETH"




    # Create a new Spotify playlist
    my_playlist = sp.user_playlist_create(
		user=username, name=f"{crypto_name} {crypto_value_change}", public=True, description="Songs inspired by crypto price changes"
	)

    # Add tracks to the playlist
    sp.user_playlist_add_tracks(username, my_playlist["id"], song_uris)

    # Return the playlist ID
    return my_playlist["id"]
