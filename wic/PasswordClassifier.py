import pickle

class PasswordClassifier:
    def __init__(self, filename):
        with open(filename, 'rb') as file:
            self.classifier = pickle.load(file)
    
    def predict(self, value):
        return self.classifier.predict(value)

    @property
    def model(self):
        '''
        Typically it is not necessary to access the MLPClassifier model directly,
        but may come in handy for debugging or using other modules that require it
        '''
        return self.classifier.model