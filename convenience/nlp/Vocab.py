from pandas import DataFrame, Series, concat

################################################################################
#                                                                          VOCAB
################################################################################
class Vocab(object):
    """
    Vocabulary object, that stores frequency counts of words from some corpus,
    along with methods for trimming down the vocabulary size based on max
    number of items, and min frequency count.

    Allows you to convert from token strings to word indices, and vice versa.
    """
    ############################################################################
    # ==========================================================================
    #                                                                   __INIT__
    # ==========================================================================
    def __init__(self):
        self.vocab = DataFrame()
        self.w2i = Series() # word to index Series
        self.i2w = Series() # index to word Series
        self.size = 0       # vocab size

    def from_tokenized_lists(self, toklist):
        print("Extracting the vocab from a tokenized list")
        self.vocab = dict()
        for sentence in toklist:
            for word in sentence:
                # If the word exists in wordcount, increment the value by 1. Otherwise
                # create a new key, initialised to 0, and increment by 1.
                self.vocab[word] = self.vocab.get(word, 0) + 1

        self.vocab = Series(self.vocab)
        self.vocab.sort_values(ascending=False, inplace=True)
        self.vocab = concat([Series({u"UNKNOWN":0}), self.vocab], ignore_index=False)
        self.w2i = Series(range(self.vocab.size), index=self.vocab.index)
        self.i2w = self.vocab.index
        self.size = self.vocab.size
        print("---Done!")