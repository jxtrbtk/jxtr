# ###############################################79############################
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Module jxtr, common helpers and tools

This module "t" contains 1 class "Say"
The prupose is to define and use a syllabic representation of positive integers
A syllab is build with 1 consonant in lower case and 1 vowel in upper case
A word is build with 2 syllabs
Words are separated by "-"
The alpĥabet has 6 vowels and 20 consonants, so a syllab can depict 120 numbers
and a word of 2 syllabs can then depict 120*120 = 14_440 numbers.

Example:
    Integer 11_566 is encoded by the string "JiVu"
    JiVu can be visually easier to read, say and remember
    Can be use as a timestamp for file,
    as a friendly depiction of a phone number or any other number

Pronunciation rules:
    Vowels:
        a: /a/, /ɑ/
        e: /ɛ/
        i: /i/
        o: /o/
        u: /y/, /ɥ/
        y: /aj/
    Consonants:
        B: /b/
        C: /ʃ/ (ch)
        D: /d/
        F: /f/
        G: /ɡ/
        H: .
        J: /ʒ/
        K: /k/
        L: /l/
        M: /m/
        N: /n/
        P: /p/
        Q: /kw/
        R: /ʁ/
        S: /s/
        T: /t/
        V: /v/
        W: /w/
        X: /ɡz/, /ks/
        Z: /z/

"""
# #############79##############################################################
#                                      #
__author__ = "jxtrbtk"                 #
__contact__ = "ByHo-BoWa-DiCa"         #
__date__ = "Ka-QoRy-CiPu"              # Sat Dec 28 22:23:31 2019
__email__ = "yeah[4t]free.fr"          #
__version__ = "2.0.0"                  #
#                                      #
# #######################################################79####################

import time

class Say:

    """Syllabic depiction of positive integer

    "Code" embed a positive integer, a list of syllabs index
    and several strings format.
    "Code" has several constructors from a string or an int

    Properties:
        value: integer inner value
        code: string representation in syllabs, words separated
        reverse: code reversed
        swap: string formatted syllabs swapped, most significant word first
    """
    #static constant
    _CONSONANT = tuple("aeiouy".lower())
    _VOWEL     = tuple("bcdfghjklmnpqrstvwxz".upper())
    _SEPARATOR = "-"
    _WORD_SIZE = 2
    _MIN_SIZE  = 2
    

    def __init__(self, number=None, code=None, swap=True, reverse=False):
        """Init method

        Arguments:
            number: positive integer, inner value (default: unix epochs is seconds)
            swap: boolean, True = higher weight syllab first (default: True)
            reverse: boolean, if the code string is reversed (default: False)
        """
        if number is None:
            number = int(time.time())
        self.__value = number
        self.__swap = swap
        self.__reverse = reverse
        if code is not None:
            self.code = code

    """
    value (property): integer inner value
    """
    def get_value(self):
        return self.__value

    def set_value(self, number):
        self.__value = number
    
    value = property(get_value, set_value)

    """
    code (property): syllabic representation
    """
    def get_code(self):
        return self.__format(self.__encode(self.__value))

    def set_code(self, str_code):
        self.value = self.__decode(str_code)

    code = property(get_code, set_code)
    #alias
    phrase = code

    """
    swap (property): put higher syllabs first when formatting
    """
    def get_swap(self):
        return self.__swap

    def set_swap(self, val):
        self.__swap = val

    swap = property(get_swap, set_swap)

    """
    reverse (property): reverse when formatting
    """
    def get_reverse(self):
        return self.__reverse

    def set_reverse(self, val):
        self.__reverse = val

    reverse = property(get_reverse, set_reverse)
    
    def __encode(self, int_value, syllab_list=None):
        """__encode method is used recursively to create a list of syllab index,
        each index represent a syllab and each syllab represent a 0 to 119 integer
        this is a base 120 syllab encoding

        Arguments:
            int_value: positive integer to add to the syllab index list
            syllab_list: list of syllab index already found
        
        Example:
            #zero value
                jxtr.t.Say(0)
                > "BaBa"
            #one value
                jxtr.t.Say(1) 
                > "BaCa"
            #default value (now)
                jxtr.t.Say()  
                > "Ka-QoRy-QiGi"
            #default value (now)
                jxtr.t.Say(code="Ka-QoRy-QiGi").value  
                > 1577569484
                
        """
        syllabs = [v+c for c in self._CONSONANT for v in self._VOWEL]
        base = len(syllabs)
        if syllab_list is None: syllab_list = []
        syllab_list.append(int_value % base)
        rest = int(int_value / base)
        if rest != 0:
            syllab_list = self.__encode(rest, syllab_list)
        return syllab_list

   
    def __format(self, encoding):
        """__format method

        Arguments:
            str_code: list of syllab index already found
        """
        syllabs = [v+c for c in self._CONSONANT for v in self._VOWEL]
        code = ""
        if len(encoding) < self._MIN_SIZE:
            encoding = encoding + [0] * (self._MIN_SIZE - len(encoding))
        if self.__swap: encoding.reverse()
        for idx, val in enumerate(encoding):
            code = code + syllabs[val]
            if (len(encoding)-idx+1) % self._WORD_SIZE == 0    \
                                     and idx != len(encoding)-1:
                code = code + self._SEPARATOR
        if self.__reverse: code = "".join(reversed(code))
        return code
    
    def __decode(self, str_code):
        """__decode method is used transform a syllab string into a integer
        it is the reverse base 120 converting process

        Arguments:
            str_code: list of syllab index already found
        """
        syllabs = [v+c for c in self._CONSONANT for v in self._VOWEL]
        base = len(syllabs)
        str_code = str_code.replace(self._SEPARATOR, "")
        if self.__reverse: str_code = "".join(reversed(str_code))
        buffer = ""
        encoding = []
        for val in str_code:
            buffer += val
            if len(buffer) == 2:
                encoding = encoding + [syllabs.index(buffer)]
                buffer = ""
        if self.__swap: encoding.reverse()
        power = 1
        value = 0
        for val in encoding:
            value = value + val * power
            power = power * base
        return value

    def to_datetime(self):
        """to_datetime returns a datetime object integer value used as unix epoch
        """
        return time.ctime(self.__value)

    def __repr__(self):
        """overwrite of the default "to string" method
        """
        return self.code

    def __add__(self, other):
        """overwrite of built-in addition 
        """
        return Say(self.value + other.value)

    def __sub__(self, other):
        """overwrite of built-in substraction 
        """
        return Say(self.value - other.value)

    def __mul__(self, other):
        """overwrite of built-in product
        """
        return Say(self.value * other.value)

    def __truediv__(self, other):
        """overwrite of built-in division
        """
        return Say(self.value // other.value)
    
# #################################################################79##########
# local unit tests


if __name__ == "__main__":

    print("-"*79)
    print("default value = now unix epochs seconds")
    test = Say()
    print("value      : " + str(test.value))
    print("code       : " + test.code)
    test.swap = False
    print("swap       : " + test.code)
    test.reverse = True
    print("reversed   : " + test.code)
    print("date       : " + test.to_datetime())
    print("-"*79)

    print("string code for int 165  : " + Say(165).code)
    print("int value for code MaCa  : " +
          str(Say(code="MaCa").value))
    print("-"*79)

    print("value                          :", Say(1542661750).value)
    print("value for swap Ka-QiMu-SeNo    :",
          Say(code="Ka-QiMu-SeNo").value)
    print("value for code NoSe-MuQi-Ka    :",
          Say(code="NoSe-MuQi-Ka", swap=False).value)
    print("value for reverse aK-iQuM-eSoN :",
          Say(code="aK-iQuM-eSoN", swap=False, reverse=True).value)
    print("value for both oNeS-uMiQ-aK    : ",
          Say(code="oNeS-uMiQ-aK", swap=True, reverse=True).value)
    print("-"*79)

# #######################################################79####################
