import docx2txt
import glob
import pandas as pd

# Your doc file directory root path
from validation import is_verse_from_separated_line

rootdir = "D:\Dataset Scraping\Data"

defective_song_count = 0

for file in glob.glob(f'{rootdir}/*/*.docx'):
    name = file
    try:
        text = docx2txt.process(file)
        splitter = "\n\n\n\n"

        if is_verse_from_separated_line(text):
            splitter = '।।'

        initVerseLst = text.split(splitter)
        song_verse_list = []
        for i in initVerseLst:
            if i != '':
                song_verse_list.append(i)

        for i in range (len(song_verse_list)):

            single_verse = song_verse_list[i].strip()

            splited_verse = single_verse.split("\n")

            temp_list = []
            for str in splited_verse:
                if str != "":
                    temp_list.append(str)

            for j in range (len(temp_list)):
                temp_list[j] = temp_list[j].strip()
            song_verse_list[i] = (' ').join(temp_list)

        temp = name.split("\\")
        publisher_name = temp[3]
        song_id = temp[4].split('_')[0]

        df = pd.DataFrame({'Publisher': publisher_name, 'Song Id': song_id, 'Song Verse': song_verse_list})

        df.to_csv('dataset.csv', mode='a', encoding="utf-8-sig", index = False, header=None)

    except Exception as exp:
        print(exp)
        print(defective_song_count, publisher_name, song_id)
        defective_song_count += 1