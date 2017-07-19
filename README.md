# ixp_hackathon
Team "They who must not be named"

# Description

A statistical implementation of a summarizer meant to compress hours of conversation to a few sentences. It is an unsupervised model based on the paper by Nenkova et. al - “Impact of Frequency on Summarization” . Being unsupervised, our model requires minimal human intervention, is fast and is largely language agnostic resulting in a comprehensive summary.

The model also compiles a list of keywords highlighting the topic of the conversation making use of a probabilistic graphical model LDA.

The summarizer is integrated with the the Slack API which provides the functionality to summarize a long history of messages on slack into a few comprehesive bullet points.

# Libraries Required:
1) Numpy
2) NLTK
3) gensim
4) Slack Client
