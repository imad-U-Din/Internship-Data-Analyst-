import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_csv('Dataset .csv') 
reviews = df['Rating text']  

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()  
    tokens = word_tokenize(text)  
    tokens = [word for word in tokens if word.isalpha()]  
    tokens = [word for word in tokens if word not in stop_words]  
    return tokens

def analyze_sentiment(tokens):
    positive_words = []
    negative_words = []
    for token in tokens:
        analysis = TextBlob(token)
        if analysis.sentiment.polarity > 0:
            positive_words.append(token)
        elif analysis.sentiment.polarity < 0:
            negative_words.append(token)
    return positive_words, negative_words

preprocessed_reviews = reviews.apply(preprocess_text)

all_positive_words = []
all_negative_words = []

for tokens in preprocessed_reviews:
    pos_words, neg_words = analyze_sentiment(tokens)
    all_positive_words.extend(pos_words)
    all_negative_words.extend(neg_words)

def get_most_common_words(word_list, n=5):
    counter = Counter(word_list)
    return counter.most_common(n)

positive_word_freq = get_most_common_words(all_positive_words)
negative_word_freq = get_most_common_words(all_negative_words)

positive_word_freq_df = pd.DataFrame(positive_word_freq, columns=['Word', 'Frequency'])
negative_word_freq_df = pd.DataFrame(negative_word_freq, columns=['Word', 'Frequency'])

print("Most Common Positive Words:")
print(positive_word_freq_df)
print("\nMost Common Negative Words:")
print(negative_word_freq_df)

def plot_word_frequency(word_freq_df, title):
    plt.figure(figsize=(12, 6))
    plt.bar(word_freq_df['Word'], word_freq_df['Frequency'], color=(0.2,0.4,0.2,0.6))
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.xticks(rotation=0)
    plt.tight_layout()  
    plt.show()

plot_word_frequency(positive_word_freq_df, 'Most Common Positive Words')
plot_word_frequency(negative_word_freq_df, 'Most Common Negative Words')
