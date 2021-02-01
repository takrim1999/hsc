import requests
from bs4 import BeautifulSoup 

#roll = 203615
#reg = 1512601557
print("		welcome to HSC result viewer shell version")
roll = int(input("\n\nyour roll: "))
reg = int(input("your registration no: "))
board = input("your board name(all lower case): ")
print("\n\nAdditional Info:\n")
req = requests.Session()
response = req.get("http://www.educationboardresults.gov.bd/" )
soup = BeautifulSoup(response.text,"lxml")
tags = soup.find_all("td")
math = tags[56].text.split()
math = int(math[0])+int(math[2])
data = {"sr":3,"et":3,"exam":"hsc","year":2020,"board":board,"roll": roll,"reg": reg,"value_s":math,"button2":"Submit"}
response = req.post("http://www.educationboardresults.gov.bd/result.php",data = data )
soup = BeautifulSoup(response.text,"lxml")
# with open("hsc.html" , "w") as f:
# 	f.write(soup.prettify())
tags = soup.find_all("td")
for i in range(24,44,4):
	print("{} : {:15}{} : {}".format(tags[i].text,tags[i+1].text,tags[i+2].text,tags[i+3].text))
print("\n\n")
print("-"*25,tags[46].text,"-"*25)
for i in range(48,70,3):
	print("{}	{:45}{}".format(tags[i].text,tags[i+1].text,tags[i+2].text))
#25-47
#49-73