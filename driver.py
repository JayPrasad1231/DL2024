import torch
from sklearn.model_selection import train_test_split
from data_cleaning import song_dataset
from data_cleaning import return_playlist

"""
Important to Understand: Our input is a list of playlists. In order to accurately
predict the songs next in the playlist, we need to split our data into training and testing.
To do this, we decided to randomly choose 70% of songs in our playlists to be training data,
with the remaining 30% to be test data. I.e., for each playlist, we will use 70% of the songs to predict
the remaining 30% of the songs, utilizing key shared characteristics. 
"""

data = return_playlist()

train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)

train_X = []
train_Y = []
test_X = []
test_Y = []

# Can edit to include validation set --> probably should do

for i in range(len(train_data)): # 100000

    curr_playlist = train_data[i]
    known_X, known_Y = train_test_split(curr_playlist, test_size=0.3, random_state=42)
    train_X.append(known_X)
    train_Y.append(known_Y)

for i in range(len(test_data)):

    curr_playlist = test_data[i]
    known_X, known_Y = train_test_split(curr_playlist, test_size=0.3, random_state=42)
    test_X.append(known_X)
    test_Y.append(known_Y)

## Time for model creation

