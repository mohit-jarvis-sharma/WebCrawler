from stop_words import get_stop_words
from nltk.tokenize import word_tokenize
#from nltk.stem import PorterStemmer
import nltk
import string

def remove_stop_words(text_list):
    stop_words = get_stop_words('en')
    temp_list = []
    for i in text_list:
        if i not in stop_words:
            temp_list.append(i)
    return temp_list

def tokenized_text(text):
    #ps = PorterStemmer()
    #sno = nltk.stem.SnowballStemmer('english')
    lemma = nltk.wordnet.WordNetLemmatizer()
    for c in string.punctuation:
        text = text.replace(c , "")
    words = word_tokenize(text)
    #clean_words = remove_stop_words(words)
    final_list = [lemma.lemmatize(wordy).lower() for wordy in words]
    return final_list