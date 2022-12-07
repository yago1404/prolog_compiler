

def create_symbol_table(token_list: list):
    token_id_list = []
    for token in token_list:
        if "LWRCHAR" in token.token_type or "UPRCHAR" in token.token_type or ("NUMBERCHAR" in token.token_type and len(token_id_list) > 0):
            token_id_list.append(token)

    for i in token_id_list:
        print(i.token)
