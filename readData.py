#Read data
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Read data
# Getting document with known ID
'''result = db.collection('person').document('janedoe').get()
if result.exists:
    print(result.to_dict())'''

# Printing all documents in a collection
'''docs = db.collection('person').get()
for doc in docs:
    print(doc.to_dict())'''

# Querying for integers and other stuff
'''docs = db.collection('person').where("age",">=", 30).get()
for doc in docs:
    print(doc.to_dict())'''

# Querying for array stuff
'''docs = db.collection('person').where("socials","array_contains", "youtube").get()
for doc in docs:
    print(doc.to_dict())'''

# Querying using instuff
docs = db.collection('person').where("address", "in", ["London", "Milan"]).get()
for doc in docs:
    print(doc.to_dict())

