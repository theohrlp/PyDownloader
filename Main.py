from __future__ import unicode_literals
import youtube_dl
import threading
import concurrent.futures
import time

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

songs = []

threads = []

while True:     #check if files exists
    try:
        name = input("Insert the name of the file(including the extention): \n")
        temp = open(name,"r")
        temp.close()
        break
    except:
        print("There is no such file in the current directory.")
        exit(1)

start = time.perf_counter()

with open(name) as f:
    for line in f:
        songs.append(line)

'''
for song in songs:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song])
'''
def doSomething(i):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([songs[i]])

for i in range(len(songs)):
    t = threading.Thread(target=doSomething, args=[i])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(doSomething, songs)


