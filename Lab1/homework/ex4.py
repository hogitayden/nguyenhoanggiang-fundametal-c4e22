from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db['customers']

events_counts = posts.find({"ref": "events"}).count()
wom_counts = posts.find({"ref": "wom"}).count()
ads_counts = posts.find({"ref": "ads"}).count()

machine_labels = ["Events", "WOM", "Ads"]

brand_counts  = [events_counts, wom_counts, ads_counts]

from matplotlib import pyplot
pyplot.pie(brand_counts, labels = machine_labels, autopct="%.1f%%", explode=[ 0,0,0])
pyplot.title("Customer identity")
pyplot.axis('equal')

pyplot.show()