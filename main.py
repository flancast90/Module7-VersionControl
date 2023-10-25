# Finn Lancaster, 2023-10-25


def encoder(pwd):
    # Takes a password of ints, and returns the password with all digits
    # incremented by 3
    return "".join([str((int(digit) + 3) % 10) for digit in pwd])


def decoder(encoded_pwd):
    # Takes an encoded password of ints, and returns the original password
    return None


if __name__ == "__main__":
    menu = """Menu
-------------
1. Encode
2. Decode
3. Quit"""
    encoded_pwd = ""
    while True:
        print(menu)
        choice = input("Please enter an option: ")
        if choice == "1":
            pwd = input("Please enter your password to encode: ")
            encoded_pwd = encoder(pwd)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            decoded_pwd = decoder(pwd)
            print(
                f"The encoded password is {encoded_pwd}, and the original password is {decoded_pwd}."
            )
        elif choice == "3":
            break
        else:
            print("Invalid option")
