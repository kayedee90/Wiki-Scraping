import requests
import json 
from bs4 import BeautifulSoup

#define the root url
root_url = "https://country-leaders.onrender.com"
leaders_url = f"{root_url}/leaders"  #define the leader url

#function to get leaders
def get_leaders(session):
    session.get(f"{root_url}/cookie")  #requests cookies
    countries = session.get(f"{root_url}/countries").json()  #create a list of countries as json
    return {country: session.get(f"{root_url}/leaders?country={country}", cookies=session.cookies).json() for country in countries}  #create a dictionary for leaders in each country


#function to get first paragraph
def get_first_paragraph(session, url):
    html_content = session.get(url).text  #get the html content
    soup = BeautifulSoup(html_content, "html.parser")  #parse html
    paragraphs = soup.find_all("p")  #find all paragraph tags
    return " ".join(tag.text.strip() for tag in paragraphs if tag.text.strip())  #return the text of the first paragraph

# create session
session = requests.Session()

#define the get leaders data in a variable
leaders = get_leaders(session)

#save leaders data to json file
with open("leaders.json", "w") as file:
    json.dump(leaders, file)  #dump leaders data in a file

#read leaders data from file
with open("leaders.json", "r") as file:
    leaders_data = json.load(file)  #put data into a dictionary

#print leaders information in a readable format
for country, leaders in leaders_data.items():
    print(f"Country: {country}")  #print country name
    for leader in leaders:
        print(f"Name: {leader['first_name']} {leader['last_name']}")  #print leader name
        print(f"Birth Date: {leader['birth_date']}")  #print leader birth date
        print(f"Place of Birth: {leader['place_of_birth']}")  #print leader place of birth
        print(f"Wikipedia: {leader['wikipedia_url']}")  #print leader URL

        print("-----")  #separator for readability

#create variables to print
first_leader = next(iter(leaders.values()))[0]  #get first leader from the dictionary
first_paragraph = get_first_paragraph(session, first_leader["wikipedia_url"])  #get the paragraph from wikipedia
print(first_paragraph)  #print paragraph


#function to save leaders data to json
def save(leaders_per_country):
    with open("leaders.json", "w") as file:
        json.dump(leaders_per_country, file)  #save leaders to json

print(json.load(open("leaders.json")))  #print json data