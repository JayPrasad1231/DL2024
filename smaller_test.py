import random
from data_cleaning import read_songs

song_dataset = read_songs()

possible_trackURIs = random.sample(song_dataset.keys(), 250)

playlists = []

for i in range(15):

    playlists.append(random.sample(possible_trackURIs, 10))

def ret_playlists():

    return playlists

