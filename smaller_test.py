import random
from data_cleaning import read_songs

song_dataset = read_songs()

possible_trackURIs = random.sample(song_dataset.keys(), 250)

playlists = []

for i in range(15):

    playlists.append(random.sample(possible_trackURIs, 10))

def ret_playlists():

    return playlists

# VECTORIZATION OF INPUT

# MODEL TESTING

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

