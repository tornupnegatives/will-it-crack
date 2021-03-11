# Will It Crack?

Will It Crack is a RESTful service for password classification. It accepts string input representing a user password and rates it as either weak, medium, or strong. It is also capable of creating character vectors for a password based on the corpus. Classification is performed using a MLPC network with three hidden layers, each containing 500 neurons.

## About the Dataset

The dataset used to train the model came from Kaggle. It contains around 670k password entries that were classified using a series of commercial password-rating algorithms. The data originally came form the 000webhost data leak of over 3 million passwords. It is worth noting that the dataset is strongly biased toward medium passwords.
