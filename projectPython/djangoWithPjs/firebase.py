
import firebase_admin
from firebase_admin import credentials
from firebase import  firebase
# cred = credentials.Certificate("excellent-zoo-313509-firebase-adminsdk-w2wn4-39125be61d.json")
# firebase_admin.initialize_app(cred,{'databaseURL': 'https://excellent-zoo-313509-default-rtdb.asia-southeast1.firebasedatabase.app/'})

# Import database module.

firebase = firebase.FirebaseApplication('https://excellent-zoo-313509-default-rtdb.asia-southeast1.firebasedatabase.app/', None)
result = firebase.get('/excellent-zoo-313509-default-rtdb/', '')
print(result)