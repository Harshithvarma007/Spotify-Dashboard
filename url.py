import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

# Spotify API credentials
client_id = '76103a4aa68f4f119d2748b631f0af4d'
client_secret = '314185f2bfe14674a2c1fa0094c8a400'

# Get access token
def get_access_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

# Fetch track information using Spotify API
def fetch_cover_url(track_name, artist_name, access_token):
    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'q': f'track:{track_name} artist:{artist_name}',
        'type': 'track',
        'limit': 1
    }
    response = requests.get(search_url, headers=headers, params=params)
    response_data = response.json()
    if response_data['tracks']['items']:
        track = response_data['tracks']['items'][0]
        return track['album']['images'][0]['url']  # Return the URL of the album cover
    return None

# Load the dataset
file_path = 'spotify-2023.csv'
spotify_df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Get access token
access_token = get_access_token(client_id, client_secret)

# Add cover URLs to the dataset
spotify_df['cover_url'] = spotify_df.apply(lambda row: fetch_cover_url(row['track_name'], row['artist(s)_name'], access_token), axis=1)

# Save the updated dataframe to a new CSV file
output_path = 'spotify-2023-urls.csv'
spotify_df.to_csv(output_path, index=False)

# Display the first few rows of the updated dataframe
spotify_df.head()
