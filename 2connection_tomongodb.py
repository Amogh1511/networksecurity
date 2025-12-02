
#Server connection of MongoDB to receive data from connection we created in Cluster in 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import sys
import os
# The dotenv read from .env(private information) file and fetches value (Ex. mongo_db_key)
from dotenv import load_dotenv
load_dotenv()  # loads .env

#Setup the key
mongo_uri = os.getenv("mongo_db_key")
uri = mongo_uri

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    #send me back the ping if connection is successfully connected to database client
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e,sys)
