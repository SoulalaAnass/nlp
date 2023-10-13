import nltk

####make file ready for NLTK###
file = open("chile corpus.txt", 'r')
file_contents = file.read()
tokenized_raw_text = nltk.word_tokenize(file_contents)
final_text = nltk.Text(tokenized_raw_text)

######investigate specific words in a file######

###count word frequencies
print("Word frequency of climate:", final_text.count("climate"))

###see words in context
print("Concordance of climate:")
final_text.concordance("climate")

###see words that appear in similar contexts
print("Words similar to climate:")
final_text.similar("climate")
