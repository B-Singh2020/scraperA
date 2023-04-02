import json
import sys
import timeit
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#firebase, get srive account file with credentials to get to your personal project (firestore) and id

cred = credentials.Certificate('service-account.json') ## intialize connection to db
app = firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'affirmations').document(u'0')   #access connection and get specific document (id)

doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')

# read json file into list
try:

    f = open('data.json')  # open file

    data = json.load(f)  # load in json data as dictionary and close file
    f.close()
    json_data = data  # set data as json obj dictionary
except Exception as e:
    print(f'FILE EXCEPTION: {str(e)}')



#iterate through list and upload objects into firestore collection (document id is same as id field )

for index, jObj in enumerate(json_data):
    if index < len(json_data):
        db.collection(u'affirmations1').document(str(index+1)).set(json_data[index])
