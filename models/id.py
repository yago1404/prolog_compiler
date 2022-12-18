class Id:
    def __init__(self, token, token_id):
        self.token = token
        self.id = token_id

    def __str__(self):
        return 'token -> "' + self.token + '", id -> ' + str(self.id)

    def __repr__(self):
        return self.__str__()
