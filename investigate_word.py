import nltk

####make file ready for NLTK###
file = open("filteredtext.txt", 'r')
file_contents = file.read()
tokenized_raw_text = nltk.word_tokenize(file_contents)
final_text = nltk.Text(tokenized_raw_text)

######investigate specific words in a file######

###count word frequencies
print("Word frequency of metaverse:", final_text.count("metaverse"))

###see words in context
print("Concordance of metaverse:")
final_text.concordance("metaverse")

###see words that appear in similar contexts
print("Words similar to metaverse:")
final_text.similar("metaverse")
