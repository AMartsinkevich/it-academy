class SuperStr(str):

    def is_repeatance(self, s):
        return not self.__str__().replace(s, '')

    def is_palindrom(self):
        return self.__str__() == "".join(reversed(self.__str__()))


if __name__ == '__main__':

    string = SuperStr('abab')
    print(string)
    print(string.is_repeatance('aba'))
    print(string.is_repeatance('ab'))
    print(string.is_palindrom())
    string = SuperStr('abba')
    print(string.is_palindrom())
