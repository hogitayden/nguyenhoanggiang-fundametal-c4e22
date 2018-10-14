from youtube_dl import YoutubeDL

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=hcAdlom3aX0'])

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=dWlnwlJlOwY', 'https://www.youtube.com/watch?v=-y3h9p_c5-M'])

# options = {
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=-y3h9p_c5-M'])

# options = {
#     'default_search': 'ytsearch', 
#     'max_downloads': 1 
# }
# dl = YoutubeDL(options)
# dl.download(['Misirlou'])

options = {
    'default_search': 'ytsearch', #không thể thay key
    'max_downloads': 1,           #có thể thay key  
    'format': 'bestaudio/audio'   #có thể thay key
}
dl = YoutubeDL(options)
dl.download(['Gucci đôn chề'])