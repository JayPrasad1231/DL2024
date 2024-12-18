# data cleaning
import json
import pandas as pd
import pickle
import random

song_dataset = {}

def read_songs():
    with open("songs.pkl", "rb") as file:
        song_dataset = pickle.load(file)
        return song_dataset
    
song_dataset = read_songs()

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
    

# populate_songs("song_data.csv")
read_songs()
res = []

# file_names = file_names of all the slices (1000 of them)
# file_names = [f"mpd.slice.{i * 1000}-{i * 1000 + 999}.json" for i in range(1000)]

# for file_name in file_names:
#     res.extend(clean_data(file_name))

def return_playlist():
    return res
