from torch import nn
from sklearn.model_selection import train_test_split
from data_cleaning import read_songs
from smaller_test import ret_playlists
from model import SongRecommenderMLP

"""
Important to Understand: Our input is a list of playlists. In order to accurately
predict the songs next in the playlist, we need to split our data into training and testing.
To do this, we decided to randomly choose 70% of songs in our playlists to be training data,
with the remaining 30% to be test data. I.e., for each playlist, we will use 70% of the songs to predict
the remaining 30% of the songs, utilizing key shared characteristics. 
"""

data = ret_playlists()

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


# VECTORIZATION OF INPUT

song_dataset = read_songs()



# MODEL TRAINING

# import torch.optim as optim

# input_size = ...  # Number of features in your song representation
# hidden_size = 128  # Hyperparameter you can tune
# output_size = len(song_dataset)  # Number of possible song recommendations (or size of embedding)

# model = SongRecommenderMLP(input_size, hidden_size, output_size)
# criterion = nn.CrossEntropyLoss()  # Or MSELoss depending on target type
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# # Training loop
# num_epochs = 20
# for epoch in range(num_epochs):
#     model.train()
#     for i, (x_batch, y_batch) in enumerate(train_loader):
#         optimizer.zero_grad()
#         outputs = model(x_batch)
#         loss = criterion(outputs, y_batch)
#         loss.backward()
#         optimizer.step()

#     print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")
