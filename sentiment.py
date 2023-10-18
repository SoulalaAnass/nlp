from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

#Read text from a file
file_path = 'filteredtext.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

#Analyze text
sentiment_scores = analyzer.polarity_scores(text)

#Map the sentiment score to a scale of 1 to -1
compound_score = sentiment_scores['compound']

if compound_score > 0:
    sentiment_mapped = 1
elif compound_score < 0:
    sentiment_mapped = -1
else:
    sentiment_mapped = 0

print(f"Sentiment (Mapped): {sentiment_mapped}")
