import docx2txt
import glob
import pandas as pd
from sortedcollections import OrderedSet

# Your doc file directory root path
rootdir = "D:\Dataset Scraping\Data"

count = 0

for file in glob.glob(f'{rootdir}/*/*.docx'):
    name = file
    try:
        text = docx2txt.process(file)

        song_verse_set = OrderedSet(text.split('\n\n\n\n'))
        song_verse_list = list(song_verse_set)

        temp = name.split("\\")
        publisher_name = temp[3]

        df = pd.DataFrame({'Publisher': publisher_name, 'Song Id': count, 'Song Verse': song_verse_list})
        print(song_verse_list)

        df.to_csv('Dataset_output.csv', mode='a', encoding="utf-8-sig", index = False, header=None)
        count = count+1

        print(count)
    except Exception as exp:
        print(exp)