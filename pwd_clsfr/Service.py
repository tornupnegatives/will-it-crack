from Vectorizer import Vectorizer
from PasswordClassifier import PasswordClassifier

class Service:
    def __init__(self, vectorizer_path, model_path):
        self.vectorizer = Vectorizer(vectorizer_path)
        self.model = PasswordClassifier(model_path)

    def single_request(self, request):
        user_input = self.vectorizer.encode([request])
        pred = self.model.predict(user_input)
        return self.parse_prediction(pred)
        
    def parse_prediction(self, prediction):
        pred = prediction[0]

        if pred == 0:
            return 'weak'
        if pred == 1:
            return 'medium'
        if pred == 2:
            return 'strong'