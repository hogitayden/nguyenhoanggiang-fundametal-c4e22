text = input('Write your words here! ')
alphabet = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w']
for i in range(len(alphabet)):
    count = text.count(alphabet[i])
    if count == 0:
        print(end='')
    else:    
        print(alphabet[i], ': ', count)

