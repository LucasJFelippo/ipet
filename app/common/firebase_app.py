from threading import Lock

import firebase_admin
from firebase_admin import credentials, firestore


class FirebaseAppMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class FirebaseAPP(metaclass=FirebaseAppMeta):
    def __init__(self) -> None:
        self.credentials = credentials.Certificate('.secrets/ipet-78c55-firebase-adminsdk-a3q4j-959f551afb.json')
        self.app = firebase = firebase_admin.initialize_app(self.credentials)
        self.database = firestore.client()

firebaseApp = FirebaseAPP()