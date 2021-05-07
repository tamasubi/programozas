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
                   



        
#create a user instance
tamas = User("example@examle.com", "Lajos", True, '1234')
print(str(tamas))
tamas.getName()





#rint("90",users)

#print("92",users[0])

#print("94",users[0].getEmail())



#FINGING A USER IN THE USER'S ARRAY

print("find",User.findByEmail("test@test.com"))
print(User.findByEmail("kamu@yes.rus"))


#FIND ALL USER

print(User.findAll())


# User.login('test@test.com', '12345')
#   - keressuk ki a usert a megadott email apajan
#   - helyes e a jelszava a usernek (isPasswordValid() fuggveny)
#   - ha helyes, visszaadja a usert
#   - ha nem hibauzenet

# user.delete()
#  - az adott user tunjon el az adatbazisbol






#User login
print("login", User.login( "test@test.com", "32"))



#registering user

User.register("emailmarhajo", "geza", True, "25")
User.register("test@test.com", "testname", False, "32")

user = User.findByEmail("test@test.com")

#isPasswordValid
print(user.isPasswordValid("2"))
print(user.isPasswordValid("32"))


#User delete
user.delete()

print(User.findAll())

