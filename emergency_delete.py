import firebase_admin
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred_obj = firebase_admin.credentials.Certificate('key.json')
app = firebase_admin.initialize_app(cred_obj)

db = firestore.client()
doc_ref = db.collection(u'classes')

term_to_delete = '' #ie 'Spring 2019'

if len(term_to_delete) != 0:
    query = doc_ref
    query = query.where(filter=FieldFilter('term', '==', term_to_delete)).stream()

    for doc in query:
        doc.reference.delete()

print('done')