import nltk
import stylecloud

with open("corpus/articles.txt", 'r') as file:
    file_contents: str = file.read()
tokenized_raw_text = nltk.word_tokenize(file_contents)
final_text = nltk.Text(tokenized_raw_text)

# investigate a document

# show how many (different) words and punctuation symbol a file contains
print("Number of tokens: ", len(final_text))
print("Number of types: ", len(set(final_text)))
print("Lexical richness of the text:", len(set(final_text)) / len(final_text))

# obtain a sorted list of vocabulary items
print("Sorted vocabulary list:", sorted(set(final_text)))

# generate similar text
print("Text generation:")
final_text.generate()

# create a word-cloud of your file
stylecloud.gen_stylecloud(file_path="corpus/articles.txt", icon_name="fas fa-apple-alt")
print("Word frequency of Metaverse:", final_text.count(":Metaverse"))
print("Concordance of Metaverse:")
final_text.concordance("Metaverse")

print("Words similar to Metaverse:")
final_text.similar("Metaverse")
