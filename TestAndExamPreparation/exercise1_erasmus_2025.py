password = input("Tell me your password: ")

if password:
    print('The first letter you entered was: ', password[0].upper())
else:
    print('It was an empty password, not good :(')
    print('Please, try again!')