import re

# open text file of 2008 NH primary Obama speech
import os
os.chdir(r'C:\Users\jorda\OneDrive\Python_Camp\python_summer2021\Day5\Lab')

with open("obama-nh.txt", "r") as f:
	obama = f.readlines()

## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]
teststrings = []
teststrings = ["there", "I'm the one,", "There", "rather"]

print(obama)

#re.findall(r"the", teststrings)
for i in teststrings:
    print(re.findall(r" the ", i))


# TODO: print lines that contain a word of any length starting with s and ending with e



## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = 'Please enter a date in the following format: 08.18.21'





