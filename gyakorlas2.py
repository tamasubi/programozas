#ebban taroljuk a usereket
users = []

class User():
    def __init__(self, email, name, premium, password):
        self.email = email
        self.name = name
        self.premium = premium
        self.password = password
        self.signincount = 0

    def __str__(self):
        return "The users email is {} the name is {} the number of sign in is {} and is a {} user.".format(self.email,self.name,self.signincount,self.premium)

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


    @classmethod
    def register(cls, email, name, premium, password):
        user = cls(email, name, premium, password)
        users.append(user)








#create a user instance
tamas = User("example@examle.com", "Lajos", True, '1234')
print(str(tamas))
tamas.getName()



#registering user

User.register("emailmarhajo", "geza", True, "25")
User.register("test@test.com", "testname", False, "32")

print(users)

print(users[0])






# User.register('test@test.com', '12345'), EZT CSINLAD MEG!
# User.login('test@test.com', '12345')
# User.signout('test@test.com')

# user.delete!
 

