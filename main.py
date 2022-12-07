from typing import Tuple
from models.token import Token
from symbol_table.create_symbol_table import create_symbol_table
from utils.token_definition import tokens_definition
import sys


def parse_cast_list_to_string(input_cast: list) -> str:
    input_cast_string = ""
    for cash_map in input_cast:
        input_cast_string = input_cast_string + cash_map['letter']
    return input_cast_string


# Check if token is exist based on token tokens_definition
def check_valid_token(string: str) -> tuple[bool, list]:
    tokens = []
    for token_type in tokens_definition:
        if tokens_definition[token_type].count(string) > 0:
            # return True, token_type
            tokens.append(token_type)
    return (True, tokens) if len(tokens) > 0 else (False, [])


# convert token cast list in string and check if token_list_string exist based on token tokens_definition
def check_valid_cast(cash_list: list) -> tuple[bool, list]:
    string_cash = ""
    for cash_map in cash_list:
        string_cash = string_cash + cash_map['letter']
    return check_valid_token(string_cash)


def main():
    args = sys.argv
    letter_map_list = []
    token_list = []
    input_cast = []
    current_line = 0

    # read file to input
    f = open(args[1] if len(args) > 1 else "./teste.pro", "r")

    # read letters in te document and save position in the doc
    for line in f:
        current_column_position = 0
        current_line = current_line + 1
        for letter in line:
            if letter == "%":
                break
            if letter != " " and letter != "\n":
                letter_map_list.append({"letter": letter, "column": current_column_position, "line": current_line})
            current_column_position = current_column_position + 1

    # check validation of token from the file and save in cast if not valid
    for letter_map in letter_map_list:
        # check if exist, if True add letter to cast and check validator of the token and check if token is valid
        # and clear cast if True
        if len(input_cast) > 0:
            input_cast.append(letter_map)
            cast_validate_tuple = check_valid_cast(input_cast)
            if cast_validate_tuple[0]:
                input_cast_string = parse_cast_list_to_string(input_cast)
                token_list.append(Token(letter_map['column'], letter_map['line'], input_cast_string,
                                        cast_validate_tuple[1]))
                input_cast = []
            elif check_valid_token(letter_map['letter'])[0]:
                input_cast.pop()
                raise Exception("Prolog Lexical Error. \"" + parse_cast_list_to_string(input_cast) + "\" is not recognized")

        # check if the letter is a simple Token, if is a Token add to list and continue file read
        elif check_valid_token(letter_map['letter'])[0]:
            token_list.append(Token(letter_map['column'], letter_map['line'], letter_map['letter'],
                                    check_valid_token(letter_map['letter'])[1]))
        # if not recognized and cast is empty, add to cast
        else:
            input_cast.append(letter_map)

    # check if cast have letters in EOF. If True, is not valid
    if len(input_cast) > 0:
        input_cast_string = parse_cast_list_to_string(input_cast)
        raise Exception("Prolog Lexical Error. The argument \'" + input_cast_string + "\' not recognized")
    if token_list[len(token_list) - 1].token != ".":
        raise Exception(
            "Prolog Lexical Error. \"" + token_list[len(token_list) - 1].token + "\" is not a terminal symbol")
    print('The lexical compiled archive is valid')

    create_symbol_table(token_list)


if __name__ == '__main__':
    main()
