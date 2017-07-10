import random


class PasswordGenerator:
    def __init__(self):
        try:
            dictionary = open('dictionary.txt')
            self.__words = set()
            for word in dictionary:
                self.__words.add(word.strip('\n'))
        except FileNotFoundError:
            raise Exception("Dictionary is missing; word passwords not possible")
            
        try:
            self.__used = open('usedpass.txt', 'r+')
            self.__usedwords = set()
            for line in self.__used:
                self.__usedwords.add(line)
        except FileNotFoundError:
            self.__used = open('usedpass.txt', 'w')

    def randChars(self):
        r = random.SystemRandom()
        # sets up all the preferred characters
        lowletter = list('abcdefghijklmnopqrstuvwxyz_')
        upletter = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        nums = list('1234567890')
        specialChar = list('!@#$%^&*()_\|/?{}')

        passwrd = []
        for x in range(r.randrange(8, 17)):
            # lowletter is used twice to add a password-like balance
            char = [r.choice(lowletter), r.choice(lowletter), r.choice(upletter), r.choice(nums), r.choice(specialChar)]
            passwrd.append(r.choice(char))
        passwrd = ''.join(passwrd)

        if passwrd+"\n" not in self.__usedwords:
            # adds the new password to the used file, to avoid repeats
            self.__used.write('{}\n' .format(passwrd))
            return passwrd
        else:
            # recurses to get an unused password if not unique
            self.randChars()

    def longRand(self):
        # repeat of randChars, with a higher char count
        # meant for more security
        r = random.SystemRandom()

        lowletter = list('abcdefghijklmnopqrstuvwxyz_')
        upletter = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        nums = list('1234567890')
        specialChar = list('!@#$%^&*()_\|/?{}')

        passwrd = []
        for x in range(r.randrange(16, 36)):
            char = [r.choice(lowletter), r.choice(lowletter), r.choice(upletter), r.choice(nums), r.choice(specialChar)]
            passwrd.append(r.choice(char))
        passwrd = ''.join(passwrd)

        if passwrd not in self.__usedwords:
            self.__used.write('{}\n' .format(passwrd))
            return passwrd
        else:
            self.longRand()

    def l33t(self, string):
        # meant to be called in case a password needs some nums
        # and special characters
        r = random.SystemRandom()
        l33tChars = {'a':'@','A':'4','e':'3','E':'3','i':'1','I':'!','o':'0','O':'0','b':'8','B':'8','g':'&','G':'&',
                     's':'5','S':'$','t':'7','T':'7','z':'2','Z':'2','l':'|','L':'1','h':'#','H':'#'}

        newleet = list(string)
        for x,y in enumerate(newleet):
            yn = r.choice([True,False])
            if yn:
                if y in l33tChars:
                    newleet[x] = l33tChars[y]

        return ''.join(newleet)

    def securePass(self):
        # has a maximum length of 35, using random choice
        # of 3-6 words with any length pulled from the dictionary.
        r = random.SystemRandom()
        passwrd = r.sample(self.__words, r.randrange(3,7))
        while len(''.join(passwrd)) > 35:
            passwrd = r.sample(self.__words,r.randrange(3,7))

        passwrd = ''.join(passwrd)
        return passwrd

    def shortSecure(self):
        # has a char maximum of 18, and max 4 words
        r = random.SystemRandom()
        passwrd = r.sample(self.__words, r.randrange(2,5))
        while len(''.join(passwrd)) > 18:
            passwrd = r.sample(self.__words, r.randrange(2,5))

        passwrd = ''.join(passwrd)
        return passwrd
