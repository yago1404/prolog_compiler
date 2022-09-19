class Token:
    def __init__(self, column_position: int, row_number: int, token: str, token_type: str):
        self.column_position = column_position
        self.row_number = row_number
        self.token = token
        self.token_type = token_type

    def __str__(self):
        return "token -> \"" + self.token + "\" token type -> " + self.token_type + " column -> " + \
               str(self.column_position) + " line -> " + str(self.row_number)

    def __repr__(self):
        return self.__str__()
