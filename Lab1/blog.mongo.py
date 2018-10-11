from pymongo import MongoClient
uri = "mongodb://admin:c4e22lab1@ds121343.mlab.com:21343/c4e22hogi"

# Connect to database

client = MongoClient(uri)
db = client.get_default_database()

# Collection
posts = db['post'] #thay connection name thi se vao duoc 1 ngan du lieu khac

post_list = posts.find()
for p in post_list:
    print(p['author'])
    print(p['title'])
    print(p['content'])


# Document
# Creat a document
# post = {
#     'title': 'Hoa sắp gặp bố mình',
#     'content': 'Ông ấy là tổng thống',
#     'author': 'Khó'
# }

# # Insert created document
# posts.insert_one(post)
