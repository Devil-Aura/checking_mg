from pymongo import MongoClient

# Replace with your MongoDB URI
MONGO_URI = "mongodb+srv://<tyuvie>:<lxYx2uM6elNxd9BR>@cluster0.ybi1b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    # Initialize the client
    client = MongoClient(MONGO_URI)

    # Test connection
    client.server_info()  # Will raise an exception if the connection fails
    print("Connection successful!")

except Exception as e:
    print("Connection failed!")
    print(f"Error: {e}")
