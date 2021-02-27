from api.Vectorizer import Vectorizer
from api.PasswordClassifier import PasswordClassifier

vectorizer = Vectorizer('models/vectorizer.pkl')
model = PasswordClassifier('models/model.pkl')

def rate_pwd(pwd):
    user_input = vectorizer.encode([pwd])
    pred = model.predict(user_input)
    
    pwd_class = parse_prediction(pred)
    return {"rating": pwd_class}

def parse_prediction(prediction):
    pred = prediction[0]

    if pred == 0:
        return 'weak'
    if pred == 1:
        return 'medium'
    if pred == 2:
        return 'strong'
