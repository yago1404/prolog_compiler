from models.token import Token
from utils.token_definition import tokens_definition


# Check if token is exist based on token tokens_definition
def check_valid_token(string: str) -> (bool, str):
    for token_type in tokens_definition:
        if tokens_definition[token_type].count(string) > 0:
            return True, token_type
    return False, ''


# convert token cast list in string and check if token_list_string exist based on token tokens_definition
def check_valid_cash(cash_list: list) -> (bool, str):
    string_cash = ""
    for cash_map in cash_list:
        string_cash = string_cash + cash_map['letter']
    return check_valid_token(string_cash)


def main():
    letter_map_list = []
    token_list = []
    input_cast = []
    current_line = 0

    # read file to input
    f = open("./teste.txt", "r")

    # read letters in te document and save position in the doc
    for line in f:
        current_column_position = 0
        current_line = current_line + 1
        for letter in line:
            if letter != " " and letter != "\n":
                letter_map_list.append({"letter": letter, "column": current_column_position, "line": current_line})
            current_column_position = current_column_position + 1

    # check validation of token from the file and save in cast if not valid
    for letter_map in letter_map_list:
        if check_valid_token(letter_map['letter'])[0]:
            token_list.append(Token(letter_map['column'], letter_map['line'], letter_map['letter'],
                                    check_valid_token(letter_map['letter'])[1]))
            input_cast = []
        elif len(input_cast) > 0 and check_valid_cash(input_cast)[0]:

            input_cast = []
        else:
            input_cast.append(letter_map)

    # check if cast have letters in EOF. If True, is not valid
    if len(input_cast) > 0:
        input_cast_string = ""
        for cash_map in input_cast:
            input_cast_string = input_cast_string + cash_map['letter']
        raise Exception("Prolog Lexical Error. The argument \'" + input_cast_string + "\' not recognized")
    if token_list[len(token_list) - 1].token != ".":
        raise Exception("Prolog Lexical Error. \"" + token_list[len(token_list) - 1].token + "\" is not a terminal symbol")
    print('The lexical compiled archive is valid')


if __name__ == '__main__':
    main()
