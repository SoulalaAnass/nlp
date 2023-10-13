######Named Entity Recognition######

import spacy

file = open("Scripts/corpus/articles.txt", "r")
file_contents = file.read()

nlp = spacy.load("en_core_web_sm")
doc = nlp(file_contents)
print([(X.text, X.label_) for X in doc.ents])
