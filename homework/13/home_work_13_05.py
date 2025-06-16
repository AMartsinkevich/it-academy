class SuperStr(str):

    def is_repeatance(self, s):
        return False if self.__str__().replace(s, '') else True

    def is_palindrom(self):
        return True if self.__str__() == "".join(reversed(self.__str__())) else False


if __name__ == '__main__':

    string = SuperStr('abab')
    print(string)
    print(string.is_repeatance('aba'))
    print(string.is_repeatance('ab'))
    print(string.is_palindrom())
    string = SuperStr('abba')
    print(string.is_palindrom())
