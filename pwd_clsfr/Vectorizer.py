import pickle

class Vectorizer:
    def __init__(self, filename):
        with open(filename, 'rb') as file:
            self.vectorizer = pickle.load(file)

    def encode(self, text):
        return self.vectorizer.transform(text)

    def tokenize(self, word):
      chars = []
      for i in word:
        chars.append(i)
      return chars

    def export(self, filename):
      with open(filename, 'wb') as file:
        pickle.dump(self.vectorizer, file)

    @property
    def vocabulary(self):
      return self.vectorizer.vocabulary_