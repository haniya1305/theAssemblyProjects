import random
import string

class shortener: 
    token_length = 10

    def __init__(self, token_length = None):
        self.token_length = token_length if token_length is not None else 5

    def issue_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.token_length))

