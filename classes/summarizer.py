from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import numpy as np

class FrequencySummarizer:
  def __init__(self, min_cut=0.1, max_cut=0.9):
    """
     Initilize the text summarizer.
     Words that have a frequency term lower than min_cut
     or higer than max_cut will be ignored.
    """
    self._min_cut = min_cut
    self._max_cut = max_cut
    self._stopwords = set(stopwords.words('english') + list(punctuation))

  def _compute_frequencies(self, word_sent):
    """
      Compute the frequency of each of word.
      Input:
       word_sent, a list of sentences already tokenized.
      Output:
       freq, a dictionary where freq[w] is the frequency of w.
    """
    freq = {}#defaultdict(int)
    for s in word_sent:
      for word in s:
        if word not in self._stopwords:
          if word not in freq.keys():
            freq[word] = 1
          else:
            freq[word] += 1

    # frequencies normalization and fitering
    # m = float(max(freq.values()))
    # for w in list(freq):#.keys():
    #   freq[w] = freq[w] / (m * 1.0)
    #   if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
    #     del freq[w]
    total = sum(freq.values())
    for w in freq.keys():
      freq[w] /= (total * 1.0)
    return freq

  def summarize(self, text, n):
    """
      Return a list of n sentences
      which represent the summary of text.
    """
    sents = sent_tokenize(text)
    assert n <= len(sents)
    req_sents = ""#[]
    SW = set(stopwords.words('english') + list(punctuation))
    word_sent = [word_tokenize(s.lower()) for s in sents]# if word_tokenize(s.lower()) not in list(SW)]
    self._freq = self._compute_frequencies(word_sent)

    for iterator in range(n):
      ranks = []
      for i,sent in enumerate(word_sent):
        score = 1.0
        for w in sent:

          if w in self._freq.keys():
            if self._freq[w] != 0:
              #print("yo!",  w)
              score *= self._freq[w]
        score *= (len(sent) * 1.0)
        ranks.append(score)
      indices = np.array(range(len(word_sent)))
      inds = np.array(ranks).argsort()
      sents_idx = indices[inds]
      req_sents += sents[sents_idx[0]]
      for w in word_sent[sents_idx[0]]:
        # print(w, self._freq[w])
        if w in self._freq.keys():
          self._freq[w] *= self._freq[w]
      word_sent.remove(word_sent[sents_idx[0]])
      sents.remove(sents[sents_idx[0]])

    # i = 1
    # for j in sents_idx[0:n]:
    #   print(i, " -> ", sents[j])
    #   i += 1
    return req_sents

#Sample usage

# fs = FrequencySummarizer()
# print(fs.summarize(text, 8))


