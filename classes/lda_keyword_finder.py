import sys
import re
import gensim
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models

class LdaKeywordsFinder:

    def __init__(self, doc="", num_topics=1, num_words=20, passes=200):
        self._doc = doc 
        self._num_topics = num_topics
        self._num_words = num_words
        self._passes = passes

    def organizeLDAResult(self, result, print_flag=False):
        _result = []
        num_topic = 1
        for i, j in result:
            keywords = []
            if print_flag is True:
                print("===topic : " + str(num_topic) + "===")
            num_topic += 1
            j = j.split(" + ")
            for k in j:
                if print_flag is True:
                    print(re.findall(r'"([^"]*)"', k)[0].encode("utf-8"))
                keywords.append(re.findall(r'"([^"]*)"', k)[0].encode("utf-8"))
            if print_flag is True:
                print("")
            _result.append(keywords)
        return _result

    def getKeywords(self):
        tokenizer = RegexpTokenizer(r'\w+')

        # create English stop words list
        en_stop = get_stop_words('en')

        # Create p_stemmer of class PorterStemmer
        p_stemmer = PorterStemmer()

        doc_set = [self._doc.decode('utf-8')]
        filler_words = ["yeah", "haha", "ll", "also", "then", "can", "will", "okay", "s", "t", "m", "or", "take", "talk", "oh", "don", "like", "guys", "just", "dad", "let","need", "plus","2", "think","one","two", "guess", "ya", "ohhh", "doesn"]


        # list for tokenized documents in loop
        texts = []

        # loop through document list
        for i in doc_set:
            
            # clean and tokenize document string
            raw = i.lower()
            tokens = tokenizer.tokenize(raw)

            # remove stop words from tokens
            stopped_tokens = [i for i in tokens if not i in en_stop and not i in filler_words ]
                
            # stem tokens
            #stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
            #print(stemmed_tokens)
            
            # add tokens to list
            #texts.append(stemmed_tokens)
            texts.append(stopped_tokens)

        # turn our tokenized documents into a id <-> term dictionary
        #dictionary = corpora.Dictionary(texts)
        dictionary = corpora.Dictionary(texts)
            
        # convert tokenized documents into a document-term matrix
        corpus = [dictionary.doc2bow(text) for text in texts]

        # generate LDA model
        
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=self._num_topics, id2word = dictionary, passes=self._passes)
        #print(ldamodel.print_topics(num_topics=10, num_words=10))
        
        return self.organizeLDAResult(ldamodel.print_topics(num_topics=self._num_topics, num_words=self._num_words))
        

if __name__ == "__main__":
    """
    reload(sys)
    sys.setdefaultencoding('utf8')
    #doc = sys.stdin.read();
    doc = open(file_name).read()
    fs = FrequencySummarizer()
    sen, result = fs.summarize(doc)
    print(result)
    for topic in result:
        for keyword in topic:
            print(keyword)
    """
