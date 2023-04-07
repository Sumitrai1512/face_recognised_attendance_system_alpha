
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    "9570":
        {
            "name": "Sumit Rai",
            "major": "Data Science",
            "starting_year": 2021,
            "total_attendance": 5,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "9543":
        {
            "name": "Madhav Jha",
            "major": "AL & ML",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "9526":
        {
            "name": "Pushpendra Singh Bist",
            "major": "Block Chain",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)