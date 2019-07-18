# SUMMARISING THE TEXT

# Importing libraries
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    import re
    import nltk
    import bs4 as bs  
    import urllib.request  
    import re
    
    
# taking the article from the wikipedia
    scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')  
    article = scraped_data.read()
    
    parsed_article = bs.BeautifulSoup(article,'lxml')
    
    paragraphs = parsed_article.find_all('p')
    
    article_text = ""
    
    for p in paragraphs:  
        article_text += p.text
    
# Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
        
# Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

# splitting into sentences  
    sentence_list = nltk.sent_tokenize(article_text)     # spliting the paragraph in sentence
 
# spliting into words
    stopwords = nltk.corpus.stopwords.words('english')   # words which are not in use like I, me, myself and all
    
    word_frequencies = {}  
    for word in nltk.word_tokenize(formatted_article_text):    # nltk.word_tokenize(p) mean split the paragraph in words
        if word not in stopwords:
            if word not in word_frequencies.keys():            # counting the word frequency
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1 
    
# finding the maximum value from the dictionary in word_frequencies
    max_frequency = max(word_frequencies.values())
    for words in word_frequencies.keys():
        word_frequencies[words] = (word_frequencies[words]/max_frequency) 
        
# Calculating sentence score- 
    sentence_scores = {}  
    for sent in sentence_list:                                   # By using word frequency we are calculating the 
        for word in nltk.word_tokenize(sent.lower()):            # total santence score
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    
# combinig the sentences
    number_sentence = 7
    import heapq  
    summary_sentences = heapq.nlargest(number_sentence, sentence_scores, key=sentence_scores.get)       
    summary = ' '.join(summary_sentences)                       # number_sentence is variable use to get best sentece of the paragraph
    print(summary)
    
            