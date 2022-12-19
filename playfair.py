# create an encrypted message using the Playfair cipher

alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

# build a 5x5 matrix of letters
def build_matrix_5x5(keyword):
    keyword = keyword.upper()
    matrix = []
    for letter in keyword:
        if letter not in matrix:
            matrix.append(letter)
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)
    return matrix

# delete spaces between letters
def delete_spaces(plaintext):
    new_plaintext = ''
    for i in plaintext:
        if i != ' ':
            new_plaintext += i
    return new_plaintext

# replace J with I
def replace_j(plaintext):
    plaintext = plaintext.upper()
    new_plaintext = ''
    for i in plaintext:
        if i == 'J':
            new_plaintext += 'I'
        else:
            new_plaintext += i
    return new_plaintext

# split the plaintext into pairs
def split_into_pairs(plaintext):
    plaintext = plaintext.upper()
    plaintext_pairs = []
    for i in range(0, len(plaintext), 2):
        plaintext_pairs.append(plaintext[i:i+2])
    return plaintext_pairs

# check if the pair has the same letter
def check_if_same_letter(plaintext_pairs):
    for i in range(len(plaintext_pairs)):
        if len(plaintext_pairs[i]) == 1:
            plaintext_pairs[i] = plaintext_pairs[i] + 'X'
        elif plaintext_pairs[i][0] == plaintext_pairs[i][1]:
            plaintext_pairs[i] = plaintext_pairs[i][0] + 'X' + plaintext_pairs[i][1]
    return plaintext_pairs

# find the position of the letter in the matrix
def find_position(letter, matrix):
    position = 0
    for i in range(len(matrix)):
        if letter == matrix[i]:
            position = i
    return position

# find the row of the letter
def find_row(letter, matrix):
    row = find_position(letter, matrix) // 5
    return row

# find the column of the letter
def find_column(letter, matrix):
    column = find_position(letter, matrix) % 5
    return column

# encrypt the plaintext
def encrypt(plaintext_pairs, matrix):
    ciphertext = ''
    for i in plaintext_pairs:
        if find_row(i[0], matrix) == find_row(i[1], matrix):
            ciphertext += matrix[find_position(i[0], matrix) + 1] + matrix[find_position(i[1], matrix) + 1]
        elif find_column(i[0], matrix) == find_column(i[1], matrix):
            ciphertext += matrix[find_position(i[0], matrix) + 5] + matrix[find_position(i[1], matrix) + 5]
        else:
            ciphertext += matrix[find_row(i[0], matrix) * 5 + find_column(i[1], matrix)] + \
                matrix[find_row(i[1], matrix) * 5 + find_column(i[0], matrix)]
    return ciphertext


# main function
def main():
    keyword = input('Enter the keyword: ')
    plaintext = input('Enter the plaintext: ')
    plaintext = delete_spaces(plaintext)
    keyword = delete_spaces(keyword)
    plaintext = replace_j(plaintext)
    keyword = replace_j(keyword)
    matrix = build_matrix_5x5(keyword)
    plaintext_pairs = split_into_pairs(plaintext)
    plaintext_pairs = check_if_same_letter(plaintext_pairs)
    ciphertext = encrypt(plaintext_pairs, matrix)
    print('The ciphertext is:', ciphertext)

if __name__ == '__main__':
    main()