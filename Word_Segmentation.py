from nltk.tokenize import sent_tokenize, word_tokenize

#Sample Text
text = """The AI, called Pluribus, defeated poker professional Darren Elias, who holds the 
record for most World Poker Tour titles, and Chris "Jesus" Ferguson, winner of six World Series of Poker events. 
Each pro separately played 5,000 hands of poker against five copies of Pluribus. In another experiment involving 
13 pros, all of whom have won more than $1 million playing poker, Pluribus played five pros at a time for a total 
of 10,000 hands and again emerged victorious."""

#Tokenize paragraph into individual sentences
nltk_sentences = sent_tokenize(text)
print("Tokenized Sentences: ", nltk_sentences)

#Tokenize paragraph/sentence into individual words
nltk_words = word_tokenize(text)
print("Tokenized Words: ", nltk_words)

#Original Text containing punctuation
text_with_punctuation = "John's burger was so! delicious that I ate it fully, #Whataburger."

#Reoving punctuation
from nltk.tokenize import RegexpTokenizer

tokenize_text = RegexpTokenizer(r'\w+') #Here \w+ is used for matching one or more word characters
Output = tokenize_text.tokenize(text_with_punctuation)
print("Text Without Punctuation:", Output)

# Removing Stop Words
text_st_words = "An apple a day keeps a doctor away, who was the person quoted this saying?"

from nltk.corpus import stopwords

#Invoke all the english stopwords
stop_word_list = set(stopwords.words('english'))

#Tokenize sentence into words
text = word_tokenize(text_st_words)

#Create an empty list and append non stop words in it

new_word_list = []
for w in text:
    if w not in stop_word_list: new_word_list.append(w)

print("Original Text:", text)
#Stop words like a, an, the are removed
print("Text after Stop Words are removed:", new_word_list)