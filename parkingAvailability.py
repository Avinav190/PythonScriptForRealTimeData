# This is a code for updating realtime parking spaces in the firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
import time

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://carspot-9d74f-default-rtdb.firebaseio.com'
})


def update_parking_Space():
    # generates random number to update parking space into a firebase
    # this program will run on raspberry pi
    return random.randint(1, 3)


ref = db.reference('ParkingSpace')

while True:
    ref.update({
          'Number': update_parking_Space(),
    })

    time.sleep(5)
