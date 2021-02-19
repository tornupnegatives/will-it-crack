from Service import Service
from Vectorizer import Vectorizer
from PasswordClassifier import PasswordClassifier
import warnings


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    service = Service('../models/vectorizer.pkl', '../models/model.pkl')

    while(True):
        # TODO: Make async loop
        password = input("Enter password: ")

        evaluation = service.single_request(password)

        print(f'Your password is {evaluation}\n')

