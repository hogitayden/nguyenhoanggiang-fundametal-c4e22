#1. Download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://dantri.com.vn"

#1.1 Connect website
conn = urlopen(url)

#1.2 Download raw data
raw_data = conn.read()

#1.3 Decode data
webpage_text = raw_data.decode("utf-8")

# print(webpage_text)
#1.4 Save text
#w = write
#b = binary

# f = open("dantri.html", "wb")
# f.write(raw_data)

# f = open("dantri.html", "w")
# f.write(webpage_text)
# f.close()

#2. Extract ROI
#2.1 Convert text to soup
soup = BeautifulSoup(webpage_text, "html.parser")
ul = soup.find("ul", "ul1 ulnew") #id="ul1 ulnew"

li_list = ul.find_all("li") #class la 1 list cac soup

news_list =  []
for li in li_list:
    h4 = li.h4
    a = h4.a   # a=li.h4.a
    title = a.string
    link = url + a["href"]

    # print(title)
    # print(link)
    news = {
        "Title": title,
        "Link": link,
    }
    news_list.append(news)
    # print("-"*20)

print(*news_list, sep="\n \n")
#print(soup.prettify())


#3. Extract data



#4. Save data
# pyexcel.save_as(records = news_list, dest_file_name = "dantri.xlsx")