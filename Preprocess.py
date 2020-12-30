from pathlib import Path
import re

# preprocess all email files.
# remove special characters , new lines , numbers from message
# remove stopword and non english words


def preProcessFiles(basepath):
    stopwords = Path("stopwords.txt").read_text().split()
    englishWords = dict.fromkeys(Path("englishWords.txt").read_text().split())
    files_in_basepath = basepath.iterdir()
    for item in files_in_basepath:
        if item.is_file():
            txt = item.read_text()
            txt = re.sub('[^A-Za-z]+', ' ', txt)
            txt = txt.lower()
            txt = txt.split()
            txt = list(dict.fromkeys(txt))
            for i in txt:
                if (i in stopwords or i not in englishWords):
                    txt.remove(i)
            txt = ' '.join(txt)
            item.write_text(str(txt))

