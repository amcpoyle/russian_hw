from pypdf import PdfReader
from deep_translator import GoogleTranslator
import time
import argparse

"""
This program will take in a pdf file that you give it through the command line,
then output a new text file to whatever directory you specify that has the
translated words side-by-side.

"""

parser = argparse.ArgumentParser("russian_hw")
parser.add_argument("file_path", help="The absolute file path of the reading", type=str)
parser.add_argument("output_path", help="Where you want the translation text file to be stored", type=str)
args = parser.parse_args()

reader = PdfReader(args.file_path)
num_pages = len(reader.pages)

start = time.time()

file_contents = []

for i in range(num_pages):
    file_contents.append("Page: {}".format(i+1))
    page = reader.pages[i]
    text = page.extract_text()

    words = text.split(" ")
    words = [''.join([j for j in i if not j.isdigit()]) for i in words]
    words = [i.strip() for i in words]
    words = [i for i in words if i != '']

    translated_words = []
    for w in words:
        translated_word = GoogleTranslator(source='ru', target='en').translate(w)
        translated_words.append(translated_word)

    for w, tw in zip(words, translated_words):
        file_contents.append("{} --- {}".format(w, tw))

    file_contents.append("------------------------------------------")
    time.sleep(15)

end = time.time()
print("Elapsed translation time: ", end - start)

with open(args.output_path, 'w', encoding='utf-8') as f:
    for line in file_contents:
        # print(line)
        f.write(f"{line}\n")