import firebase_admin
from firebase_admin import firestore
import json

cred_obj = firebase_admin.credentials.Certificate('key.json')
app = firebase_admin.initialize_app(cred_obj)

db = firestore.client()
doc_ref = db.collection(u'classes')

input_file = ''

while not input_file.endswith('.json'):
	input_file = input('Please give json file containing the distribution: ')
	input_file = input_file.replace("'","")
	if not input_file.endswith('.json'):
		print('Please give a valid json file')

with open(input_file,"r") as f:
	file_contents = json.load(f)
	
for k in file_contents:
 	doc_ref.add(k)
	 
print('done')