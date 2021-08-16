## Go to https://polisci.wustl.edu/people/88/all OR https://polisci.wustl.edu/people/list/88/all
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization 
##  	Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
##		Professor Aksoy’s research is motivated by an interest in comparative political institutions and political violence. 
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
	
from bs4 import BeautifulSoup
import urllib.request
import csv
#import lxml
import os


with open("washu_faculty.csv", "w") as f:
    w = csv.DictWriter(f, fieldnames = ("Name", "Title", "Email", "Webpage", "Specialization"))
    w.writeheader()
    web_address = 'https://polisci.wustl.edu/people/88/all'
    web_page = urllib.request.urlopen(web_address)
    soup = BeautifulSoup(web_page.read(), features = "lxml")
    # find
    s = soup.find_all("a", class_ = "card")
    #print(s[0])
    
    faculty = {} # dict
    for i in s:
        faculty["Name"] = i.h3.text
        #print(i.h3.text)
        #print()
        
        faculty["Title"] = i.find(class_ = "dept").text
        #print(i.find(class_ = "dept"))
        #print()
        
        #faculty["Email"]
        
        
        
        if i["href"][0] == "/":
            webpage = "https://polisci.wustl.edu{}".format(i["href"])
        else:
            webpage = i["href"]
        
        #print(webpage)
        new_page = urllib.request.urlopen(webpage)
        new_soup = BeautifulSoup(new_page.read(), features = "lxml")
        
        
        
        faculty["Webpage"] = webpage
        
        try:
            faculty["Email"] = new_soup.find(class_ = "detail contact").find("a")["href"]
        except:
            faculty["Email"] = "N/A"
            
        try:
            faculty["Specialization"] = new_soup.find(class_ = "post-excerpt").text
        except:
            faculty["Specialization"] = "N/A"
            
        #try:
        #    print(new_soup.find(class_ = "links").find("a")["href"]
        
        
        
        
        #print(new_soup.find(class_ = "detail contact").find("a").text)
        
        w.writerow(faculty)


    
    

# web_address = 'https://polisci.wustl.edu/people/88/all'
# web_address = 'https://polisci.wustl.edu/people/88/list/88/all'

# with open('iceland_test.csv', 'w') as f: # set up with the writer
#   w = csv.DictWriter(f, fieldnames = ("name", "party", "phone")) # define column names
#   w.writeheader() # write the header
#   web_address='https://www.althingi.is/altext/cv/en/' # the web address
#   web_page = urllib.request.urlopen(web_address) # open the web page
#   soup = BeautifulSoup(web_page.read()) # soup the web page
#   all_members = soup.find_all('tr') # find the list of names and parties
#   for i in range(1,3): # for members 1 and 2 (member 0 is just the table heading)
#     try:
#       member = {} ## empty dictionary to fill in
#       member_i = all_members[i].find_all('td') # subset lower to each individual item
#       member["name"] = member_i[0].text # member's name
#       member['party'] =  member_i[1].text # member's party
#       inner_page_url = web_address + member_i[0].a['href'] # get the extension to their personal page
#       inner_page = urllib.request.urlopen(inner_page_url) # open the personal page
#       inner_soup = BeautifulSoup(inner_page.read()) # soup the personal page
#       member['phone'] = inner_soup.find('a', {'class' : 'tel'}).text # get phone number
#     except:
#       member['name'] = 'NA'
#       member['party'] = 'NA'
#       member['phone'] = 'NA'
#     w.writerow(member) # write the row for this specific member
#     time.sleep(random.uniform(1, 5)) # be polite, sleep!


			
				
				
				
