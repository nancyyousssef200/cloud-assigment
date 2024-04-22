
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Read the contents of the file
with open("paragraphs.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Remove punctuation 
text = re.sub(r'[^\w\s]', '', text)

# Tokenize the text using NLTK's word tokenizer
words = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words  = [word for word in words if word.lower() not in stop_words]

# Count word frequencies
word_counts = Counter(filtered_words)


# Display word frequency count
for word, count in word_counts.items():
    print(f"{word}: {count}")
 
