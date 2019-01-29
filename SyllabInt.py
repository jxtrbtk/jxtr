# ###############################################79############################
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Module jxtr, common helpers and tools

This module contains 1 single class SyllabInt
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

Todo:
    * error handling
    * add padding method to force string to have a minimum number of syllabs

"""
# #############79##############################################################
#                                      #
__author__ = "jxtrbtk"                 #
__contact__ = "ByHo-BoWa-DiCa"         #
__date__ = "BeZy-QeVi-Ka"              # Tue Jan 29 12:58:20 2019
__email__ = "yeah[4t]free.fr"          #
__version__ = "1.1.0"                  #
#                                      #
# ##################################79#########################################

import time


class SyllabInt:

    """Syllabic depiction of positive integer

    SyllabInt embed a positive integer, a list of syllabs index
    and several strings format.
    SyllabInt has several constructors from a string or an int

    Properties:
        value: integer inner value
        code: string representation in syllabs, words separated
        reverse: code reversed
        swap: string representation syllabs swapped, MSB first
        both: string representation both swapped and reversed
    """
    _consos = list("aeiouy".lower())
    _voyos = list("bcdfghjklmnpqrstvwxz".upper())
    _separator = "-"

    """Init method

    Arguments:
        number: positive integer to depict (default: unix epochs is seconds)
    """
    def __init__(self, number=None):
        self._syllabs = [voyo+conso for conso in self._consos
                         for voyo in self._voyos]
        if number is None:
            number = int(time.time())
        self.value = number

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, number):
        self._value = number
        self.Refresh()

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, str):
        self.value = self.Decode(str.replace(self._separator, ""))

    @property
    def reverse(self):
        return self._reverse

    @reverse.setter
    def reverse(self, str):
        self.code = self.Reverse_String((str))

    @property
    def swap(self):
        return self._swap

    @swap.setter
    def swap(self, str):
        self.code = self.Swap_String_By2(str.replace(self._separator, ""))

    @property
    def both(self):
        return self._both

    @both.setter
    def both(self, str):
        self.swap = self.Reverse_String(str)

    """Encode method is used recursively to create a list od syllab index,
    each inde represent a syllab and each syllab represent à 0 to 119 integer
    this is a base 120 syllab encoding

    Arguments:
        int_value: positive integer to add to the syllab index list
        str_code: list of syllab index already found
    """
    def Encode(self, int_value, syllab_list):
        syllab_list.append(int_value % 120)
        rest = int(int_value / 120)
        if rest != 0:
            syllab_list = self.Encode(rest, syllab_list)
        return syllab_list

    """Decode method is used transform a syllab string into a integer
    it is the reverse base 120 converting process

    Arguments:
        str_code: list of syllab index already found
    """
    def Decode(self, str_code):
        value = 0
        power = 1
        buffer = ""
        for val in str_code:
            buffer += val
            if len(buffer) == 2:
                value = value + self._syllabs.index(buffer) * power
                power = power * 120
                buffer = ""
        return value

    """Refresh method recreates all the depictions of the inner integer
    Method is kicked at each change in the value
    """
    def Refresh(self):
        self._encoding = self.Encode(self.value, [])
        self._code = ""
        self._swap = ""
        for idx, val in enumerate(self._encoding):
            self._code += self._syllabs[val]
            self._swap = self._syllabs[val] + self._swap
            if idx % 2 == 1 and idx != len(self._encoding)-1:
                self._code += self._separator
                self._swap = self._separator + self._swap
        self._reverse = self.Reverse_String(self.code)
        self._both = self.Reverse_String(self.swap)

    """ToDateTime returns a datetime object integer value used as unix epoch
    """
    def ToDateTime(self):
        return time.ctime(self._value)

    """Reverse_String is a static method that reverse a string

    Arguments:
        string: string to reverse
    """
    @staticmethod
    def Reverse_String(string):
        return "".join(reversed(string))

    """Swap is a static method that swap string members 2 by 2

    Arguments:
        string: string to swap
    """
    @staticmethod
    def Swap_String_By2(string):
        output = ""
        buffer = ""
        for val in string:
            buffer += val
            if len(buffer) == 2:
                output = buffer + output
                buffer = ""
        return output

    """From_Int is a constructor from an positive integer

    Arguments:
        int_value: integer to use as inner value
    """
    @classmethod
    def From_Int(cls, int_value):
        return cls(int_value)

    """From_Code is a constructor from a standard syllab and word string

    Arguments:
        str_code: string code representation
    """
    @classmethod
    def From_Code(cls, str_code):
        temp = cls()
        temp.code = str_code
        return temp

    """From_Reverse is a constructor from a revereses syllab and word string

    Arguments:
        str_reverse: string code reversed representation
    """
    @classmethod
    def From_Reverse(cls, str_reverse):
        temp = cls()
        temp.reverse = str_reverse
        return temp

    """From_Swap is a constructor from a swapped syllab and word string

    Arguments:
        str_swap: string code swapped representation
    """
    @classmethod
    def From_Swap(cls, str_swap):
        temp = cls()
        temp.swap = str_swap
        return temp

    """From_Swap is a constructor from a both swapped and reversed string

    Arguments:
        str_both: string swapped and reversed
    """
    @classmethod
    def From_Both(cls, str_both):
        temp = cls()
        temp.both = str_both
        return temp

# #################################################################79##########
# local unit tests


if __name__ == "__main__":

    print("-"*79)
    print("default value = now unix epochs seconds")
    test = SyllabInt()
    print("value      : " + str(test.value))
    print("code       : " + test.code)
    print("reverse    : " + test.reverse)
    print("swap       : " + test.swap)
    print("both       : " + test.both)
    print("date       : " + test.ToDateTime())
    print("-"*79)

    print("string code for int 165  : " + SyllabInt.From_Int(165).code)
    print("int value for code MaCa  : " +
          str(SyllabInt.From_Code("MaCa").value))
    print("-"*79)

    print("value for code NoSe-MuQi-Ka    : " +
          str(SyllabInt.From_Code("NoSe-MuQi-Ka").value))
    print("value for swap Ka-QiMu-SeNo    : " +
          str(SyllabInt.From_Swap("Ka-QiMu-SeNo").value))
    print("value for reverse aK-iQuM-eSoN : " +
          str(SyllabInt.From_Reverse("aK-iQuM-eSoN").value))
    print("value for both oNeS-uMiQ-aK    : " +
          str(SyllabInt.From_Both("oNeS-uMiQ-aK").value))
    print("-"*79)

# #######################################################79####################
