from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db['post']

post = {
    'title': 'Xin chao cac ban',
    'content': 'Welcome 2 new world',
    'author': 'Hogi'
}

posts.insert_one(post)