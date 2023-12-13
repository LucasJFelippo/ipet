from app.products.classes.product import Product
from app.products.classes.tag import Tag

from app.common.firebase_app import firebaseApp
from google.cloud.firestore_v1.base_query import FieldFilter


def query_to_array(query):# -> list:
    array = []
    for element in query:
        product = element.to_dict()
        tags = []
        for tag in product["tags"]:
            tags.append(Tag(tag))
        array.append(Product(product["id"],
                             product["name"],
                             product["price"],
                             tags,
                             product["weight"],
                             product["picture"]))
    return array

def search(input = "") -> None:
    if input == "": return query_to_array(firebaseApp.database.collection("products").stream())
    content = []
    query = firebaseApp.database.collection("products").where(filter=FieldFilter("tags", "array_contains", input)).stream()
    content += query_to_array(query)
    return content