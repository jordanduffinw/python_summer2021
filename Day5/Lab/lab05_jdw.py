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
teststrings = ["there", "I'm the one,", "There", "rather", "soothe ",
               " soothe "]

#print(obama)

#re.findall(r"the", teststrings)
#for i in teststrings:
#    print(re.findall(r"\b(the|The)\b", i))

#for i in obama:
#    print(re.findall(r"\b(the|The)\b", i))
    
    
keyword = re.compile(r"\b(the|The)\b")
for i in obama:
    if not keyword.search(i):
        print(i)



# TODO: print lines that contain a word of any length starting with s and ending with e
teststrings2 = ["soothe", 'sequence', "pittsburgh", "I found the Sequence", "chop suey",
                "seethE"]
key2 = re.compile(r"\b(s|S)[a-z]*(e|E)\b")
for i in teststrings2:
    if key2.search(i):
        print(i)

for i in obama:
    if key2.search(i):
        print(i)

## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = 'Please enter a date in the following format: 08.18.21'

pattern = re.compile(r"(\d{2})\.(\d{2})\.(\d{2})")
tsearch = pattern.search(date)

print(tsearch.group())
print(tsearch.groups(1))

day = ("Day: " + tsearch.group(2))
month =("Month: " + tsearch.group(1))
year = ("Year: " + tsearch.group(3))

print(month)
print(day)
print(year)