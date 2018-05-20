import youtube_dl
from pip._internal.commands.search import print_results
from pip._vendor.html5lib.treewalkers import pprint

opts ={}
ydl = youtube_dl.YoutubeDL(opts)

with ydl:
    result = ydl.extract_info('https://www.youtube.com/watch?v=e3FkeMlGrB0',
        download=False # We just want to extract the info
    )

print(type(result))


values = result.items()

for value in values:
    print(value)
    