from models.id import Id


def create_symbol_table(token_list: list):
    token_id_list = []
    current_string = ""
    current_table_id = 0
    new_token_list = []

    for token in token_list:
        if "LWRCHAR" in token.token_type or "UPRCHAR" in token.token_type or ("NUMBERCHAR" in token.token_type and len(token_id_list) > 0):
            current_string = current_string + token.token
        elif len(current_string) > 0:
            token_id_list.append([current_string, current_table_id])
            new_token_list.append(Id(current_string, current_table_id))
            new_token_list.append(token)
            current_string = ""
            current_table_id = current_table_id + 1
        else:
            new_token_list.append(token)

    for i in token_id_list:
        print("table => " + str(i[0]) + " | " + str(i[1]))

    print(new_token_list)
