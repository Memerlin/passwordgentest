import string
import secrets  # DO NOT USE RANDOM FOR SECURITY ISSUES. DO NOT.


# The variables on the function will be used later ig
# noinspection PyShadowingNames
def generate_password(length=20, use_punctuation=False):
    alphabet = string.ascii_letters + string.digits
    punctuation = string.punctuation + alphabet
    # same here
    if not use_punctuation:
        return ''.join(secrets.choice(alphabet) for n in range(length))
    else:
        # I have no idea why this works
        return ''.join(secrets.choice(punctuation) for n in range(length))

    # I was supposed to write a multiple password generator here but I kinda forgor.

    # remember to put a variable first and then ask for input

if __name__ = "__main__": # So it doesn't run when I import this to the UI
    option = input('Enter an option to continue. \n[1]Generate a password\n[2]Generate multiple passwords\n')
    if option == '1':
        pass_len = input(
            'How many characters do you want? Please enter a numerical value.\n')  # This will result in a string
        len_int = int(pass_len)  # This converts the string to an integer (a number).
        punctuation = input('Use punctuation?\n[1]Yes\n[2]No\n')
        if punctuation == '1':
            print(generate_password(length=len_int, use_punctuation=True))
        else:
            print(generate_password(length=len_int))
    else:
        passwords = input('How many passwords do you want to generate?\n')
        pass_amount = int(passwords)
        multi_pass_len = input('How many characters do you want? Please enter a numerical value\n')
        multi_pass_len = int(multi_pass_len)
        punctuation = input('Use Punctuation?\n[1]Yes\n[2]No\n')
        if punctuation == '1':
            for i in range(pass_amount):
                print(generate_password(length=multi_pass_len, use_punctuation=True))
        else:
            for i in range(pass_amount):
                print(generate_password(length=multi_pass_len))
        print(f'Test, you requested {pass_amount} passwords.')
