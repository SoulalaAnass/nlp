from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer with your custom lexicon
analyzer = SentimentIntensityAnalyzer()
custom_lexicon_file = "your_custom_lexicon.txt"

# Load your custom lexicon
with open(custom_lexicon_file, "r", encoding="utf-8") as file:
    custom_lexicon = {}
    for line in file:
        word, score = line.strip().split()
        custom_lexicon[word] = float(score)

# Update VADER's lexicon with your custom lexicon
analyzer.lexicon.update(custom_lexicon)

# German text to analyze
german_text = "Das Produkt ist wunderbar und fantastisch."

# Analyze sentiment
sentiment_scores = analyzer.polarity_scores(german_text)

# Interpret the sentiment scores
if sentiment_scores['compound'] >= 0.05:
    sentiment = "Positive"
elif sentiment_scores['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print the sentiment and sentiment scores
print(f"Sentiment: {sentiment}")
print(f"Positive Score: {sentiment_scores['pos']:.2f}")
print(f"Negative Score: {sentiment_scores['neg']:.2f}")
print(f"Neutral Score: {sentiment_scores['neu']:.2f}")
print(f"Compound Score: {sentiment_scores['compound']:.2f}")

##underbar 2.0
# schlecht -1.5
# fantastisch 2.5
# nicht gut -1.0###
