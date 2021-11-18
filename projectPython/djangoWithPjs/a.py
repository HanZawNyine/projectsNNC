import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyD_tVzlPM3WH57oB7v_jB6iM-etO5Q9PV8",
  "authDomain": "ledblink-b7d21.firebaseapp.com",
  "databaseURL": "https://ledblink-b7d21-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "ledblink-b7d21",
  "storageBucket": "ledblink-b7d21.appspot.com",
  "messagingSenderId": "142321598197",
  "appId": "1:142321598197:web:e892f88c5e5ef9af84cfbc",
  "measurementId": "G-DBY85Y9D7H"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# data = {
#   "LED":0,
# }

#db.push(data)
#db.child("blink").set(data)
db.child('blink').update({"LED":1})
#db.child("LED").remove()

# auth = firebase.auth()
# storage = firebase.storage()

led = db.child("blink").get()
#print(led.val())
for led in led.each():
   print(led.val())