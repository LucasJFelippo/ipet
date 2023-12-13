from app.common.firebase_app import firebaseApp

class Product:
    def __init__(self, id, name, price, tags, weight, picture) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.tags = tags
        self.weight = weight
        self.picture = picture

    def register(self) -> None:
        product = {"id": self.id,
                   "name": self.name,
                   "price": self.price,
                   "tags": [tag.name for tag in self.tags],
                   "weight": self.weight,
                   "picture": self.picture
                    }
        firebaseApp.database.collection("products").document(self.id).set(product)