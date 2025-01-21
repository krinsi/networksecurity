from pymongo import MongoClient

uri = "mongodb+srv://krinsiradadiya:123@cluster0.o3dmq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)

try:
    # Test the connection
    client.admin.command('ping')
    print("Connected successfully to MongoDB!")
except Exception as e:
    print(f"Connection failed: {e}")
