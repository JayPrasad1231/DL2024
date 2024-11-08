# data cleaning
import json
import pandas as pd
import pickle

song_dataset = {}

def clean_data(spotify_million):

    with open(spotify_million, 'r') as file:
        data = json.load(file)

    playlists = data['playlists']
    new_playlists = [] # the new playlists with the changes
    differences = [] # tracks how many songs were removed (if we want to see if we should use the dataset)

    for playlist in playlists:
        songs = playlist['tracks']
        curr_playlist = []
        for song in songs:
            track_uri = song['track_uri']
            if track_uri in song_dataset:
                curr_playlist.append(track_uri)

        new_playlists.append(curr_playlist)
        differences.append(len(songs) - len(curr_playlist))

    return new_playlists


def populate_songs(spotify_dataset): 

    df = pd.read_csv(spotify_dataset)
    for idx, row in df.iterrows():
        if idx == 0:
            continue
        song_dataset[row['id']] = row

    with open("songs.pkl", "wb") as file:
        pickle.dump(song_dataset, file)

def read_songs():
    with open("songs.pkl", "rb") as file:
        song_dataset = pickle.load(file)
    

# populate_songs("song_data.csv")
read_songs()
res = clean_data("slice_1.json")

# print(res)