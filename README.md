# jxtr
This module provides a way to encode an integer in syllables. That's a tool I use sometimes to timestamp files or generate a code. (I've used this as a my first git repo...)

## Description 
This module "t" contains 1 single class Say. The prupose is to define and use a syllabic representation of positive integers
A syllab is build with 1 consonant in lower case and 1 vowel in upper case. 

A word is build with 2 syllabs. Words are separated by "-"

The alpĥabet has 6 vowels and 20 consonants, so a syllab can depict 120 numbers and a word of 2 syllabs can then depict 120*120 = 14_440 numbers.

The object can provide the code generated, a word swapped version of the code, the reverse code or with both transformations.

## Example 1:
    Integer 11_566 is encoded by the string "jIvU"
    jIvU can be visually easier to read, say and remember
    Can be use as a timestamp for file,
    as a friendly depiction of a phone number or any other number

## Example 2:
    Unix epochs 1546850909 is encoded by the string "Me-GeBe-TiKa"
    Reverse version is "aKiT-eBeG-eM"  
    Swapped version is "Ka-TiBe-GeMe"  
    Both transformations version is "eMeG-eBiT-aK"
    This represents the date "Mon Jan  7 09:48:29 2019"

## Code example :
    ### Timestamp ###
    print("default value = now unix epochs seconds")
    test = Say()
    print("value      : " + str(test.value))
    print("code       : " + test.code)
    test.swap = False
    print("swap       : " + test.code)
    test.reverse = True
    print("reversed   : " + test.code)
    print("date       : " + test.to_datetime())

    print("string code for int 165  : " + Say(165).code)
    print("int value for code MaCa  : " +
          str(Say(code="MaCa").value))

    print("value                          :", Say(1542661750).value)
    print("value for swap Ka-QiMu-SeNo    :",
          Say(code="Ka-QiMu-SeNo").value)
    print("value for code NoSe-MuQi-Ka    :",
          Say(code="NoSe-MuQi-Ka", swap=False).value)
    print("value for reverse aK-iQuM-eSoN :",
          Say(code="aK-iQuM-eSoN", swap=False, reverse=True).value)
    print("value for both oNeS-uMiQ-aK    :",
          Say(code="oNeS-uMiQ-aK", swap=True, reverse=True).value)

## Pronunciation rules:
    Vowels:
        A: /a/, /ɑ/
        E: /ɛ/
        I: /i/
        O: /o/
        U: /y/, /ɥ/
        Y: /aj/
    Consonants:
        b: /b/
        c: /ʃ/ (ch)
        d: /d/
        f: /f/
        g: /ɡ/
        h: .
        j: /ʒ/
        k: /k/
        l: /l/
        m: /m/
        n: /n/
        p: /p/
        q: /kw/
        r: /ʁ/
        s: /s/
        t: /t/
        v: /v/
        w: /w/
        x: /ɡz/, /ks/
        z: /z/
