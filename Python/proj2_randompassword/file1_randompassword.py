
import string   # to import the cases like lower, upper etc
import random   # to generate random data


class Password:

    def __init__(self, charset, length):

        self.charset = charset    # string given by user
        self.length = length      # total number of input length given by user
        self.char_array = []  # includes all the characters which should be include in password
        self.password = []
        # l = lower case
        # u = upper case
        # d = digit
        # s = special character
         
        # if user need a password which has l , u , d
        # ldu or he need ls, or l only etc


    def set_the_charset(self):
        if('l' in self.charset):
            self.char_array.append(string.ascii_lowercase)

        if ('u' in self.charset):
            self.char_array.append(string.ascii_uppercase)

        if ('d' in self.charset):
            self.char_array.append(string.digits)

        if ('s' in self.charset):
            self.char_array.append(string.punctuation)

    def get_char_array(self):
        return self.char_array

    def generate_password(self):
        print(self.char_array)

        for i in range(self.length):
            outer_index = random.randrange(0, len(self.char_array))
            inner_index = random.randrange(0, len(self.char_array[outer_index]))
            self.password.append(self.char_array[outer_index][inner_index])


    def get_password(self):
        return ''.join(self.password)




