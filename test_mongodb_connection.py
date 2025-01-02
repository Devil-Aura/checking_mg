from pymongo import MongoClient

# Replace with your MongoDB URI
MONGO_URI = "mongodb+srv://<obitospace098>:<oNk1XNORkK5MPOcU>@cluster0.mongodb.net/<@rohit098>?retryWrites=true&w=majority"

try:
    # Initialize the client
    client = MongoClient(MONGO_URI)

    # Test connection
    client.server_info()  # Will raise an exception if the connection fails
    print("Connection successful!")

except Exception as e:
    print("Connection failed!")
    print(f"Error: {e}")
