class Token:
    def __init__(self, column_position: int, row_number: int, token: str, token_type: str):
        self.column_position = column_position
        self.row_number = row_number
        self.token = token
        self.token_type = token_type

