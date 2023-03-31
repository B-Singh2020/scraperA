import requests
import json
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import timeit

from bs4 import BeautifulSoup


def return_list(order_list):
    new_list = []
    for i in order_list:
        new_list.append(i.text)

    return new_list

#pull and parse lists from url
URL = "https://gentwenty.com/affirmations-for-self-worth/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="post-49809")
job_elements = results.find_all("div", class_="entry-content mvt-content")
ol_elements = job_elements[0].find_all("ol", class_="")

#format data into list of id-string pairs

affirm_list = []
id_list = list(range(1,101))
for ol_element in ol_elements:
    li_elements = ol_element.find_all("li", class_="")
    affirm_list.extend(return_list(li_elements))

json_list = []
for i in range(100):
    json_pair = dict(id = id_list[i], affirmation = affirm_list[i])
    json_list.append(json_pair)

# Create json file of objs
json_dict = json.dumps(json_list, indent=4)
print(json_dict)
#with open("data.json", "w") as outfile:
#    outfile.write(json_dict)


## connect to firestore
cred = credentials.Certificate('service-account.json')
firebase_admin.initialize_app(cred)