#Creating records
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Adding documents with auto IDs
# db.collection('person').add({'name': 'Jane', 'age': 30 , 'employed': True})

# Setting documents with auto IDs
# db.collection('person').document('janedoe').set({'name': 'Jane', 'age': 30 , 'employed': True})

# db.collection('person').document().set({'name': 'Jane', 'age': 30 , 'employed': True})

# Meriging documents
db.collection('person').document('janedoe').set({'address': 'London'}, merge=True)

#Creating sub collection
db.collection('person').document('janedoe').collection('movies').add({'name': 'Avengers'})

db.collection('person').document('janedoe').collection('movies').document('HP').set({'name': 'Harry Potter'})