from sklearn.feature_extraction.text import CountVectorizer
import wikipedia
import nltk
import urllib.parse as urlparse
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

from youtube_transcript_api import YouTubeTranscriptApi
corpus=[]
s=''
url_data = urlparse.urlparse("https://www.youtube.com/watch?v=CFN69J7A81Y")
query = urlparse.parse_qs(url_data.query)
video = query["v"][0]
x = YouTubeTranscriptApi.get_transcript(video)
for item in x:
    s = (item["text"])
    corpus.append(s)

vocab = ["pandemic", "million", "death"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
for word in vectorizer.get_feature_names():
    if(word.isdigit() and len(word)==4):
        vocab.append(word)

keywords = ''

for term in vectorizer.get_feature_names():
    if(term in vocab):
        keywords+=(term + ' ')
        

topic = (wikipedia.search(keywords)[0])
page = wikipedia.page(topic)
summary = (wikipedia.summary(topic))
        
a_list = nltk.tokenize.sent_tokenize(summary)

num_of_keywords_wiki={}
num_of_keywords_vid={}

for sentence in a_list:
    num_of_keywords_wiki[(sum(1 for word in vocab if word in sentence))] = sentence.split(',')[0]

for sentence in corpus:
    num_of_keywords_vid[(sum(1 for word in vocab if word in sentence))] = sentence


X =(num_of_keywords_wiki[max(num_of_keywords_wiki)])
print("Wiki sentence: " + X)
print()
Y = (num_of_keywords_vid[max(num_of_keywords_vid)])
print("Video sentence: " + Y)

# tokenization  
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 

# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[] 
  
# remove stop words from the string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
  
# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0

# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine) 
print("\n")
print("Wikipedia and the video share " + str(round((cosine*100),2)) + "% similarity about: "+ str(topic))

if cosine>= .50:
    print("This is a factual statement")
elif cosine>=.35:
    print("This is a fairly facutal statement, but reccommend to do some more research")
else:
    print("This is most likely false information. Do some more research!")
    
print("Here's a link with more information: ")
print(page.url)
