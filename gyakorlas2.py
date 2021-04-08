import re
class user():

    def __init__(self, email, nev, signincount, premium, password):
        self.email = email
        self.nev = nev
        self.signincount = signincount
        self.premium = premium
        self.password = password


    def __str__(self):
        return f"The user's email is {self.email} the name is {self.nev} the number of sign in is {self.signincount} and is a {self.premium} user."


    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

def create():

    password = input("enter password")
    signincount = 0
    premium = False



    count = 0
    while True:
        email = input("enter email: ")
        nev = input("enter nev: ")
        count += 1
        if count == 3:

            break
        else:
            if nev == 'elmo' and password == 'blue':

                break
            else:
                print("menja rákba")
                # tell them it is wrong and have them retry, stay in loop
    return user(email, nev, signincount, premium, password)




Tom = create()

print(Tom.__str__())


Tom.setEmail("java@gmail.com")
print("the new email is", Tom.getEmail())


