users = []

class User
    attr_accessor :email, :name, :premium
    attr_writer :password
    attr_reader :signincount

    def initialize(email, name, premium, password)
        @email = email
        @name = name
        @premium = premium
        @password = password
        @signincount = 0
    end

    def to_s
        "The users email is #{@email} the name is #{@name} the number of sign in is #{@premium} and is a #{@password} user."
    end


end

# objektum letrehozasa
tamas = User.new('example@examle.com', "Lajos", true, '1234')

# email kilvasasa a meglevo objektumbol, es email beleirasa az objektumba
puts tamas.email
tamas.email = 'new@example.com'

# sign in count kivulrol olvashato, de nem irhato
puts tamas.signincount

# ez hibat fog dobni, mert nem irhato
# tamas.signincount = 1

# password kivulrol irhato, de nem olvashoato
tamas.password = 'new pssword'

# ez hibat fog dobni, mert nem olvashato
# tamas.password



puts tamas