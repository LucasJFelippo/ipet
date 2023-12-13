import firebase_admin
from firebase_admin import credentials, firestore

cred_obj = credentials.Certificate('.secrets/ipet-78c55-firebase-adminsdk-a3q4j-959f551afb.json')
firebase = firebase_admin.initialize_app(cred_obj)

db = firestore.client()


import json

with open('setup\populate.json') as user_file:
  items = json.load(user_file)

for key in items:
    ref = db.collection("products").document(key)
    ref.set(items[key])
