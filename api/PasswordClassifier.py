import pickle

class PasswordClassifier:
    def __init__(self, filename):
        with open(filename, 'rb') as file:
            self.model = pickle.load(file)
    
    def predict(self, value):
        return self.model.predict(value)
