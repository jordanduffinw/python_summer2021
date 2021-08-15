## 1. write the following functions
## 2. write a unittest class to test each of these functions once
## 3. Run it in this script

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    try:
        txt = txt.upper()
    except:
        raise TypeError(str.upper("This ain't a string!"))
    return txt.upper()
shout("yell")
shout(42069)

## reverse all characters in string
def reversetext(txt):
    try:
        txt[::-1]
        return txt[::-1]
    except:
        raise TypeError(str.upper("This ain't a string!"))

#reversetext("racecar") # I assume this worked
#reversetext(42069)

reversetext("this is a test")

## reverse word order in string
def reversewords(txt):
    try:
        words = txt.split(" ")
        words.reverse()
        return " ".join(words)
    except:
        raise TypeError(str.upper("This ain't a string!"))

reversewords("all cats go to heaven")
reversewords(42096)
        
           
## reverses letters in each word
def reversewordletters(txt):
    try:
        words = txt.split(" ")
        newword = []
        for word in words:
            newword.append(reversetext(word))
            print(reversetext(word))
        return " ".join(newword)
    except:
        raise TypeError(str.upper("This ain't a string!"))
        
reversewordletters("all cats go to heaven")
reversewordletters(42096)


## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?", "hi", "hello there", 5, "hope this works", 100, "will it?"]

for string in string_list:
    try:
        reversetext(string)
        print(reversetext(string))
    except:
        if TypeError:
            print(string)
        #raise TypeError(str.upper("This ain't a string!"))
        
## 2. write a unittest class to test each of these functions once
#---------- Unit Test ----------#

# Write tests before / alongside your code
# Tests the smallest possible unit of your code 
# Forces code structure
# Allows easier integration of multiple functions
# Much easier to return to code:
#    Write a test for what you want to implement next.
# Easier to make code changes
# We can easily incorporate lots of these into our work flow.
# Test-driven development

# We can use assert to test our code within our script
#assert sum([1, 2, 3]) == 6 # It will not return anything if it is correct
#assert sum([2, 3]) == 6
#assert avg(2, 2) == 2
#assert avg(2, 2) == 4

# We can also use a test runner, such as unittest

# Example
# Open file mytest.py

import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_shout(self): 
        self.assertEqual('foo'.shout, 'FOO')
    
    def test_reversetext(self):
        self.assertTrue('ooF'.reversetext()) 
        self.assertFalse('Foo'.reversetext())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string 
        # We need the keyword "with" when using self.assertRaises():
        # "with" is a keyword to use a context manager 
        # See: https://www.geeksforgeeks.org/context-manager-in-python/
        with self.assertRaises(TypeError):
            s.split(2)
# if you want to run the test with this script
if __name__ == '__main__': 
    unittest.main()	
			
			
			
			
			
			

