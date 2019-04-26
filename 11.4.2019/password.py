# password

x=1
while x <= 3:
    password = input("Enter password: ")
    correctPassword ='123456'
    if password == correctPassword:
        print('welcome')
        break

    else:
        x += 1

        if x <=3:
            print('input: ',x,". Invalid please try again", )

        else:
            print('Your account has been blocked')
        