import spacy
from spacy.tokens import Doc

file = open("corpus/articles.txt", 'r')
file_contents = file.read()

nlp = spacy.load('en_core_web_sm')
doc = nlp(file_contents)

###POS Tagging###
for token in doc:
    print("Word:", token, ";", "POS:", token.pos_)

