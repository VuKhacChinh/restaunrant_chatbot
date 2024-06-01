import gensim
import nltk
import numpy
from pyvi import ViTokenizer
from const.Constant import *


def getBagOfWords(s, words):
    bag = [0 for _ in range(len(words))]
    s = gensim.utils.simple_preprocess(s)
    s = ' '.join(s)
    s_words = ViTokenizer.tokenize(s)
    s_words = nltk.word_tokenize(s_words)
    s_words = [w for w in s_words if w not in stop_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)