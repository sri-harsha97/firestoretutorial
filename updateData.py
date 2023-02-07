#Update data
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


#Update Data - known key
#db.collection('person').document('janedoe').update({'address':'Glasgow'})
#db.collection('person').document('janedoe').update({'age':firestore.Increment(10)})


#Update Data - Arrays - known key
#db.collection('person').document('janedoe').update({'socials':firestore.ArrayRemove(['instagram','youtube'])})
#db.collection('person').document('janedoe').update({'socials':firestore.ArrayUnion(['instagram','youtube'])})


#Update data - Unknown Key
#First Method
'''docs = db.collection('person').get()
for doc in docs:
    if doc.to_dict()['age'] > 30:
        key = doc.id
        db.collection('person').document(key).update({"agegroup":"middle aged"})'''

#Second Method
docs = db.collection('person').where('age', '<', 35).get()
for doc in docs:
        key = doc.id
        db.collection('person').document(key).update({"agegroup": "young"})

