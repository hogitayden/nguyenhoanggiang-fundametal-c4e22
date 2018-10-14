#1. Download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'https://www.apple.com/itunes/charts/songs/'

#1.1 Connect website
connect = urlopen(url)

#1.2 Download raw data
raw_data = connect.read()

#1.3 Decode data
web_text = raw_data.decode('utf-8')

# print(web_text)
#1.4 Save text
# f = open('itunes.html', 'wb')
# f.write(raw_data)
# f.close()

#2. Extract ROI
#2.1 Convert text to soup
soup = BeautifulSoup(web_text, "html.parser")
section = soup.find("section", "section chart-grid")
ul = section.div.ul
li_list = ul.find_all('li')
new_list = []

for li in li_list:
    a1 = li.h3.a
    a2 = li.h4.a
    song_names = a1.string
    artists = a2.string
    news = {
        "Song's name": song_names,
        "Artists": artists,
    }
    new_list.append(news)

# print(*new_list, sep ='\n \n')

#4. Save data
# pyexcel.save_as(records = new_list, dest_file_name = "itunes.xlsx")


#Part 2: Download
from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,           
    'format': 'bestaudio/audio'  
}
dl = YoutubeDL(options)
for i in new_list:
    dl.download(i)