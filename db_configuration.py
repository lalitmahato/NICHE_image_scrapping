from pymongo import MongoClient

# Database Configuration
user = 'scrapper'
password = 'HmmoJWT1yIWSRmQV'
database = 'images'
connection_str = "mongodb+srv://" + user + ":" + password + "@hck.k9ax4.mongodb.net/?retryWrites=true&w=majority"
# database connection setup
client = MongoClient(connection_str)
db = client.get_database(database)
