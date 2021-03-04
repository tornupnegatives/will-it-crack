from api.Vectorizer import Vectorizer
from api.PasswordClassifier import PasswordClassifier

vectorizer = Vectorizer('models/vectorizer.pkl')
model = PasswordClassifier('models/model.pkl')

def rate_pwd(pwd):
    user_input = vectorizer.encode([pwd])
    pred = model.predict(user_input)
    
    pwd_class = parse_prediction(pred)
    return {"rating": pwd_class}

def tokenize(pwd):
   user_input = vectorizer.encode([pwd])

   # Get tokens
   tokens = user_input.tocoo().col

   decoded = []
   vocab = vectorizer.vocabulary
   for token in tokens:
      original = list(vocab)[list(vocab.values()).index(token)]
      decoded.append(original)

   # Get tf-idf
   scores = user_input.tocoo().data

   # Zip results into JSON object
   embedding = {}
   for i in range(len(decoded)):
      embedding[decoded[i]] = scores[i]

   return {'embedding': embedding}

def parse_prediction(prediction):
    pred = prediction[0]

    if pred == 0:
        return 'weak'
    if pred == 1:
        return 'medium'
    if pred == 2:
        return 'strong'
