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
    def setSignInCount(self, signincount):
        self.signincount = signincount

    def getSignInCount(self):
        return self.signincount

    def setPremium(self, premium):
        self.premium = premium

    def getPremium(self):
        return self.premium

    def setPassword(self, password):
        self.password = password

    
#nem akarjuk hogy barki lassa
    def getPassword(self):
        return self.password

    def delete(self):
        users.remove(user)
                
    def isPasswordValid(self, password):
        if self.getPassword() == password: 
            return True
        else:
            return False

    @classmethod
    def register(cls, email, name, premium, password):
        user = cls(email, name, premium, password)
        users.append(user)

    @classmethod
    def findByEmail(cls, email):
        for user in users:
            if user.getEmail() == email:
                return user
        return None

    @classmethod
    def findAll(cls):
        return users
    

    @classmethod
    def login(cls, email, password):
        user = cls.findByEmail(email)

        if user is None:
            print("email or password not valid")
            return None
        
        if user.isPasswordValid(password):
            incrementedSignInCount = user.getSignInCount() + 1
            user.setSignInCount(inceremtedSignInCount)

            print("Welcome {}".format(email))
            return user
        else:
            print("email or password not valid")
                   





        
# User instance
tamas = User("example@examle.com", "Lajos", True, '1234')

# User instance string representation
print(str(tamas))

# User instance getter
tamas.getName()


# User methods
User.register("emailmarhajo@example.com", "geza", True, "25")
User.register("test@test.com", "testname", False, "32")

allUsers = User.findAll()
print(allUsers)

# User successfully found (user instance)
User.findByEmail("emailmarhajo@example.com")

# User was not found found (None)
User.findByEmail("nincsilyenemail@example.com")

user = User.login('emailmarhajo@example.com', "25")
user.isPasswordValid("123")
user.delete()
print(allUsers)
