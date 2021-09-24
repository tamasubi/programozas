$users = []

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

    def delete
        $users - [self]
    end

    def password_valid?(password)
        @password == password
    end

    class << self
        def register(email, name, premium, password)
            user = new(email, name, premium, password)
            $users << user
        end
    end
end

# objektum letrehozasa
tamas = User.new('example@examle.com', "Lajos", true, '1234')

#objektum string formaban a to_s miatt
puts tamas

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

#user registration
User.register('emailmarhajo@example.com', 'geza', true, '25')

# users tomb kiirasa, ahova beleregisztratuk az uj usert
puts $users


tamas.delete

puts $users

puts tamas.password_valid?('new pssword')