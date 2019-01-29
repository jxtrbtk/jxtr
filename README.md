# jxtr
This module provides a way to encode an integer in syllables. That's a tool I use sometimes to timestamp files or generate a code. (I've used this as a my first git repo...)

## Description 
This module contains 1 single class SyllabInt. The prupose is to define and use a syllabic representation of positive integers
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
    Unix epochs 1546850909 is encoded by the string "mEgE-bEtI-kA"
    Reverse version is "Ak-ItEb-EgEm"  
    Swapped version is "kA-tIbE-gEmE"  
    Both transformations version is "EmEg-EbIt-Ak"
    This represents the date "Mon Jan  7 09:48:29 2019"

## Code example :
    ### Timestamp ###
    test = SyllabInt()    # note: default value is now unix epochs
    print("value      : " + str(test.value))
    print("code       : " + test.code)
    print("reverse    : " + test.reverse)
    print("swap       : " + test.swap)
    print("both       : " + test.both)
    print("date       : " + test.ToDateTime())

    ### Constructors ###
    print("string code for int 165  : " + SyllabInt.From_Int(165).code)
    print("int value for code mAcA  : " +
          str(SyllabInt.From_Code("mAcA").value))
    print("value for code nOsE-mUqI-kA    : " +
          str(SyllabInt.From_Code("nOsE-mUqI-kA").value))
    print("value for swap kA-qImU-sEnO    : " +
          str(SyllabInt.From_Swap("kA-qImU-sEnO").value))
    print("value for reverse Ak-IqUm-EsOn : " +
          str(SyllabInt.From_Reverse("Ak-IqUm-EsOn").value))
    print("value for both OnEs-UmIq-Ak    : " +
          str(SyllabInt.From_Both("OnEs-UmIq-Ak").value))

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
