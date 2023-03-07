def encode(password):
    encode_list = []
    for i in range(len(password)):
        if int(password[i]) + 3 >= 10:
            x = int(password[i]) - 10
        else:
            x = int(password[i])
        encode_list.append(x + 3)
    encode_str = ' '
    for num in encode_list:
        encode_str += str(num)
    return encode_str