from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd

search = input('type "s" to start wikiScrap, type "q" to exit:')
if search == 'q' or search == 'Q':
    print("Quiting...")
    exit()
else:
    print("Creating .txt file ...")
    file = open('input.txt', 'a+', encoding='utf-8')
    url ="https://public.boxcloud.com/api/2.0/internal_files/413465789782/versions/437018393782/representations/text/content/?access_token=1!URUi9eABUoDw-7g-z-utebtVH3-OmA_Xrp2HgFdGss0Gmq-j3jO7AxiT1A7D2xwiNAXW12OYJnzrWcRMA3PWW3Iz3d9ij6sdM0CgkuQ08hbIakZ2Iev0aa1eCxibi46I1g4oP3Egvg6X7riDne8MXYdyhNhWOdoe1lxlOAIVnKXjqwY3bF8UGpGfWBlXDSO6Ptc3AWpltx42m1yISPezsjpUKGflHtSsBYnEaBokMvY_-LOWKiIXLg2176k0AW3KwXe6UQhEioD3wS74e84L4BQxKIVUM6rPx1R9a82wfbqBx1vbBVZ_a5g1dgdX9rMEfQgt_XvLecXxXL7Xw9SmM96mghcLkcj5V3kB5tpwyE5tmcjaJA0aZr6TY6SWqfhhxdw1lalOOIVivo6-6HQgtuZg3vnMD93ca5v5pgsuFf80ePL8mJepggIdc61mU1WtEUordE-RXoXd7sgcfPKV0VuNLDo7aprmJAyPf9YmGHDCBo6SCSrS5Pk7FnWBEA0pQJ3x_jYAAn9A_ekp2ecRQ8fZZtXMkDZmT-uHwN46LuCTAF7zPxSgWARz2iTsILQ.&shared_link=https%3A%2F%2Fumkc.app.box.com%2Fs%2F7by0f4540cdbdp3pm60h5fxxffefsvrw&box_client_name=box-content-preview&box_client_version=2.36.0"
    headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser') 
    file.write(str(soup))
    print(soup)

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

#Opening the saved input Files
sentence = open('input.txt', encoding="utf8").read()

# Tokenization
stokens = nltk.sent_tokenize(sentence)
wtokens = nltk.word_tokenize(sentence)

print("\nWord  Tokenization:\n")
print(wtokens)
print("\nSentence  Tokenization:\n")
print(stokens)
    
# Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("\nPOS / Lemmatization\n")

for t in wtokens:
        print("Lemmatizer:", lemmatizer.lemmatize(t), ",    With POS=a:", lemmatizer.lemmatize(t, pos="a"))

# Trigram
from nltk.util import ngrams
print("\nTrigram\n")
trigrams=ngrams(wtokens,3)
trigram_list=[]
for trigram in trigrams:
    trigram_list.append(trigram)
    print(trigram)
    
#Caluclating Frequency   
wordFreq=nltk.FreqDist(trigram_list)
top_ten=wordFreq.most_common(10)
print("Top 10 Repeated Trigrams\n",top_ten) 


#Check sentences
concate=""

for j in range(len(top_ten)):
    for sen in stokens:
        token = nltk.word_tokenize(sen)
        trigrams = list(ngrams(token, 3))
        if top_ten[j][0] in trigrams:
            print("-->",sen)
            concate=concate+" "+sen

   
print("\n#################### Concatation of Sentences ######################\n",concate)

