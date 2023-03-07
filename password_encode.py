# joseph cuenco

def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def encode(password):
    encoded_pass = ''
    for i in password:
        i = int(i)
        i += 3
        if i >= 10:
            x = i % 10
            i = x
        i = str(i)
        encoded_pass += i
    return encoded_pass


def decode(password):
    decoded_pass = ''
    for i in password:
        i = int(i)
        i -= 3
        if i < 0:
            i += 10
        decoded_pass += str(i)
    return decoded_pass


def main():
    encoded_pass = ""
    loop = True
    while loop is True:

        print_menu()

        user_option = int(input('Please enter an option: '))

        if user_option == 1:
            pass_to_encode = input('Please enter your password to encode: ')
            encoded_pass = encode(pass_to_encode)
            print('Your password has been encoded and stored!')
            print()

        elif user_option == 2:
            print(f"The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.\n")

        elif user_option == 3:
            break


if __name__ == '__main__':
    main()
