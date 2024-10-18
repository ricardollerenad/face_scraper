import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

# Verificar las variables de entorno
print("MONGO_URI:", os.getenv("MONGO_URI"))
print("MONGO_DB:", os.getenv("MONGO_DB"))
print("MONGO_COLLECTION:", os.getenv("MONGO_COLLECTION"))

"""
# Cargar las variables desde el archivo .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

def test_upload_to_mongodb(data):
    # Crear cliente de MongoDB
    client = MongoClient(MONGO_URI)

    # Acceder a la base de datos y colección
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]

    try:
        # Intentar insertar el documento en la colección
        result = collection.insert_one(data)
        print(f"Inserted post with ID: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cerrar la conexión
        client.close()

if __name__ == "__main__":
    # Datos de prueba para insertar
    test_data = {
        'post_id': '12345',
        'post_url': 'https://www.facebook.com/some_post',
        'post_type': 'text',
        'reactions': '5',
        'comments': [],
        'views': '100'
    }
    test_upload_to_mongodb(test_data)
"""