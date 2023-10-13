from typing import TextIO
from nltk.corpus import stopwords
import nltk

####make file ready for NLTK###
file = open("corpus/articles.txt", 'r')
file_contents = file.read()
tokenized_raw_text = nltk.word_tokenize(file_contents)
final_text = nltk.Text(tokenized_raw_text)

####printing stopwords
nltk.download('stopwords')


stops = set(stopwords.words('german'))
# print(stops)

stops = set(stopwords.words('english'))
# print(stops)


### stopword removal on an example sentence

example_sent = """This is a sample sentence, showing off the stop words filtration."""

stop_words = set(stopwords.words('english'))

word_tokens = nltk.word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence.clear()

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

### stopword removal on a file

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

file = open("corpus/articles.txt", 'r')
line = file.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile: TextIO = open("corpus/articles.txt", 'a')
        appendFile.write(" " + r)
        appendFile.close()
