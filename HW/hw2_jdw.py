### Assignment: go to https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks
# Create a .csv file with the following infrmation for each spoken address given by President Biden since
# he became President on 2021-01-20:
    # - Date of spoken address
    # - Title
    # - Full text of address or remarks
    # - Citation/footnoote (if one exists)
# Remember, be polite and sleep after accessing each individual document page!

### Importing libraries -- All these might not actually get used, but I saw them used before
from bs4 import BeautifulSoup
import csv
import lxml.html as lh
import os
import sys
import time
import random
import requests
import urllib.request

### Ben said we wouldn't need these, but just in case:
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup as bs
# from selenium.webdriver.common.keys import Keys

### Setting my directory -- Dunno if you'll need this to grade, though.
os.chdir(r'C:\Users\jorda\OneDrive\Python_Camp\python_summer2021\HW')

with open("hw2_jdw.csv", "w", newline = "") as f:                                   # Setting up the writer
    w = csv.DictWriter(f, fieldnames = ("Date", "Title", "Remarks", "Citation"))    # Defining the column names of the csv
    w.writeheader()                                                                 # Writing the header
    speeches = {}                                                                   # Creating our dictionary of speeches

    ### The tricky thing here is getting BeautifulSoup to go from one page to the next and terminate when I want it to.
    ### The 'j' loop cycles each page of the UCSB database, and (as of 8/18/21) Biden's speeches go back to the 20th page.
    ### I don't know how to tell the loop to terminate after the start date of 1/20/21, however.
    ### Instead, I've got it terminating once we get to President Trump.
    ### Having range(21) seems safer than having a while loop that moves indefinitely, too.

    for j in range(21):
        web_address = "https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks?page={}".format(j)
                                                                                        # Defining the web address
        web_page = urllib.request.urlopen(web_address)                                  # Opening the web page
        soup = BeautifulSoup(web_page.read(), features = "lxml")                        # Souping up the web page
        s = soup.find_all(class_ = "row")                                               # Creating the list of speeches
        
        for i in s:                                                                     # Creating the loop
            inner_page_url = "https://www.presidency.ucsb.edu" + i.a["href"]            # Getting the inner pages for each speech
            
            if inner_page_url == "https://www.presidency.ucsb.edu/documents/presidential-documents-archive-guidebook":
                continue                                                                # There's a documentation page we don't care about
                                                                                        # So we skip it
            
            inner_page = urllib.request.urlopen(inner_page_url)                         # Opens to the page for said speech
            inner_soup = BeautifulSoup(inner_page.read())                               # Soups the page
            
            if inner_soup.h3.text == "Donald J. Trump":                                 # Ends the program once we get back to President Trump
                break
            
            print(inner_soup.h3.text)                                                   # Testing the code via print
            print(i.h4.text)                                                            # This shows us how far along we are
            speeches["Date"] = i.h4.text                                                # Storing the dates
            
            speeches["Title"] = inner_soup.h1.text                                      # Collects the title of the speech
            print(inner_soup.h1.text)
            print(inner_page_url) 
            print()
            
            ### Note! Microsoft Excel cannot read any cells with more than 32,767 characters. Any more causes the program to freak out.
            ### I've added an if-statement that skips addresses that long, for the sake of spot-checking the HW file. That being said,
            ### opening the CSV in something like RSTudio shows that the longer addresses were indeed inscribed into the CSV correctly.
            ### By default, I'm leaving the if-statement in.
            
            for allwords in inner_soup.find_all("p"):                                   # Collects the text of every speech
                #print(inner_soup.find(class_ = "field-docs-content").text)
                if len(inner_soup.find(class_ = "field-docs-content").text) > 32767:
                    continue
                speeches["Remarks"] = inner_soup.find(class_ = "field-docs-content").text
                
            ### Note: for some reason, the speech text is encoded with an empty line before the text begins.
            ### when viewing "Remarks" in Microsoft Excel, the cell appears to be empty until you actually click on it.
            
            for allwords in inner_soup.find_all(class_ = "field-prez-document-citation"):
                                                                                        # Collects citations for every speech
                #print(inner_soup.find("p", class_ = "ucsbapp_citation").text)
                speeches["Citation"] = inner_soup.find("p", class_ = "ucsbapp_citation").text
           
            w.writerow(speeches)                                                        # Recording the row for this csv
            time.sleep(random.uniform(1, 5))                                            # 'Cuz we're POLITE
