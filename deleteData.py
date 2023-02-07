#Delete datagit
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#Delete - known ID
#db.collection('person').document('Johndoe1').delete()

#Delete specific field - known Id
#db.collection('person').document('Johndoe').update({"social":firestore.DELETE_FIELD})

#Delete document unknown id
'''docs = db.collection('person').get()
for doc in docs:
    key = doc.id
    db.collection('person').document(key).delete()'''


#Second Method

'''docs = db.collection('person').where('age', '<', 35).get()
for doc in docs:
        key = doc.id
        db.collection('person').document(key).delete()'''



docs = db.collection('person').where('age', '<', 35).get()
for doc in docs:
        key = doc.id
        db.collection('person').document(key).update({"social":firestore.DELETE_FIELD})