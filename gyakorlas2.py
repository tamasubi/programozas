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


tamas = User("example@examle.com", "Lajos", True, '1234')
print(str(tamas))
tamas.getName()



# User.register('test@test.com', '12345'), EZT CSINLAD MEG!
# User.login('test@test.com', '12345')
# User.signout('test@test.com')

# user.delete!
 