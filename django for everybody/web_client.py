import urllib.request

fhand = urllib.request.urlopen("http://127.0.0.1:9000/romeo.txt")
for line in fhand:
    print(line.decode().strip())
    
    
#1:10:44 DJ4E