def main():
    alphabet_hash = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                     'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                     'X': 24, 'Y': 25, 'Z': 26}
    alphabet_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    user_input = input("Enter a string: ").upper()
    length = 2 * alphabet_hash[user_input] - 1
    result = [user_input] * length
    result_init = result.copy()
    print(convert_string(result_init))
    
    i = 1
    init_i = 0
    j = length - 2
    index_alpha = alphabet_hash[user_input] - 1
    
    if index_alpha != 0:
        while j != init_i:
            if i <= j:
                for index in range(i, j + 1):
                    result[index] = alphabet_list[index_alpha - 1]
            else:
                for index in range(j, i + 1):
                    result[index] = alphabet_list[index_alpha + 1]
            
            if i <= j:
                index_alpha -= 1
            else:
                index_alpha += 1
            i += 1
            j -= 1
            print(convert_string(result))
        print(convert_string(result_init))


def convert_string(array):
    return ''.join(array)


if __name__ == "__main__":
    main()
