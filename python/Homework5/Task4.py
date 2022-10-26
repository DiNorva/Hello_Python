""" 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
Входные и выходные данные хранятся в отдельных текстовых файлах.
Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d 
или 11a3b7c1d => aaaaaaaaaaabbbcccccccd """



with open('file_encode.txt', 'w', encoding='UTF-8') as data:
    data.write('aaaaaaabbbbbbcccccccccd')

with open('file_encode.txt','r', encoding='UTF-8') as data:
    string = data.readline()

def encode(decode_string):
    encode_string = ''
    count = 1
    char = decode_string[0]
    for i in range(1, len(decode_string)):
        if decode_string[i] == char:
            count += 1
        else:
            encode_string = encode_string + str(count) + char
            char = decode_string[i]
            count = 1
            encode_string = encode_string + str(count) + char
    return encode_string

def decode(encode_string):
    decode_string = ''
    new_char = ''
    for i in range(len(encode_string)):
        if encode_string[i].isdigit():
            new_char += encode_string[i]
        else:
            decode_string += encode_string[i] * int(new_char)
    print(decode_string)


with open('file_encode.txt', 'r', encoding='UTF-8') as data:
    decode_string = data.read()

with open('file_decode.txt', 'w', encoding='UTF-8') as data: 
    encode_string = encode(decode_string)
    data.write(encode_string)

print(f'Декодированная строка: {decode_string}')
print(f'Закодированная строка: {encode(decode_string)}')







# решение со стрима 

# original_string = 'aaaaaaabbbbbbcccccccccd'

# my_dict = {}

# for letter in original_string:

#     if not my_dict.get(letter):
#         my_dict[letter]= original_string.count(letter)

# result_string = ''

# for k, v in my_dict.items():
#     result_string += str(k) + str(v)

# print(result_string)



