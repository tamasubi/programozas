class User():
    def __init__(self, email, name, premium, password):
        self.email = email
        self.name = name
        self.premium = premium
        self.password = password
        self.signincount = 0

    def __str__(self):
  #      return f"The user's email is {self.email} the name is {self.name} the number of sign in is {self.signincount} and is a {self.premium} user."
        return '1'

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

#nem szetteljuk, mert belulrol allitja magat
#   def setSignInCount(self, signincount):
#        self.signincount = signincount

    def getSignInCount(self):
        return self.signincount

    def setPremium(self, premium):
        self.premium = premium

    def getPremium(self):
        return self.premium

    def setPassword(self, password):
        self.password = password

#nem akarjuk hogy barki lassa
#    def getPassword(self):
#        return self.password


Tamas = User("example@examle.com", "Lajos", True, '1234')
print(str(Tamas))



# def create():

#     password = input("enter password")
#     signincount = 0
#     premium = False



#     count = 0
#     while True:
#         email = input("enter email: ")
#         nev = input("enter nev: ")
#         count += 1
#         if count == 3:

#             break
#         else:
#             if nev == 'elmo' and password == 'blue':

#                 break
#             else:
#                 print("menja rakba")
#                 # tell them it is wrong and have them retry, stay in loop
#     return user(email, nev, signincount, premium, password)

# Tom = create()

# print(Tom.__str__())


# Tom.setEmail("java@gmail.com")
# print("the new email is", Tom.getEmail())
