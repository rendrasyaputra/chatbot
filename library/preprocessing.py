import re
import string
from library.spell_checker import correction
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# membuat stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# function untuk pre-processing
def preprocess(text):
    # melakukan case folding
    text = text.lower()
   
    # menghilangkan nomor dan tanda baca
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
   
    # melakukan tokenizing
    words = text.split()
   
    # melakukan spell check
    corrected_words = []
    for word in words:
        corrected_words.append(correction(word))

    # melakukan stemming
    stemmed_words = []
    for word in corrected_words:
        stemmed_words.append(stemmer.stem(word))
       
    # melakukan filtering stopwords
    with open('library/data-stopword.txt', 'r') as file:
        stopwords = file.read().splitlines()
    filtered_words = [word for word in stemmed_words if word not in stopwords]
   
    print("Hasil case folding: ", text)
    print("Hasil penghilangan nomor dan tanda baca: ", text)
    print("Hasil tokenizing: ", words)
    print("Hasil koreksi : ", corrected_words)
    print("Hasil stemming: ", stemmed_words)
    print("Hasil filtering stopwords: ", filtered_words)
    
    # menggabungkan kata yang telah dilakukan preprocessing
    preprocessed_text = ' '.join(filtered_words)

    print("Pattern :",preprocessed_text)
    return preprocessed_text