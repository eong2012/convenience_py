# GloVe Word Embeddings

## Download
There are different embeddings that are trained on different text data.

- `glove.6B`
    - Wikipedia 2014 + Gigaword 5
    - 6B tokens, 400K vocab, uncased
    - 50d, 100d, 200d, & 300d vectors,
    - 822 MB download
    - URL = http://nlp.stanford.edu/data/glove.6B.zip

- `glove.42B.300d`
    - Common Crawl
    - 42B tokens, 1.9M vocab, uncased
    - 300d vectors,
    - 1.75 GB download
    - URL = http://nlp.stanford.edu/data/glove.42B.300d.zip

- `glove.840B.300d`
    - Common Crawl
    - 840B tokens, 2.2M vocab, cased
    - 300d vectors
    - 2.03 GB download
    - URL = http://nlp.stanford.edu/data/glove.840B.300d.zip

- `glove.twitter.27B`
    - Twitter
    - 2B tweets, 27B tokens, 1.2M vocab, uncased
    - 25d, 50d, 100d, & 200d vectors,
    - 1.42 GB download
    - URL = http://nlp.stanford.edu/data/glove.twitter.27B.zip
```

Use one of the embedding names from the above list, and download it by running wget on the command line.

```sh
# Chose embedding name (NOTE: no spaces on either side of the = sign)
EMBEDDING_NAME=glove.6B

# Download embeddings
BASE_URL=http://nlp.stanford.edu/data/
wget -c ${BASE_URL}${EMBEDDING_NAME}.zip

# Extract from zip file
unzip ${EMBEDDING_NAME}.zip -d ${EMBEDDING_NAME}
```

## Process in Python

### METHOD 1. Use the same ordering as GloVe embeddings file

```py
# TODO:
```


### METHOD 2. Use your own word ordering

**TODO:** Deal with "UNKNOWN" token

Given your own vocabulary that you have specified, and a mapping between word strings and their index, as in the following simplified example.

```py
id2word = ["king", "queen", "man", "woman", "lizard"]
word2id = {word:id for id, word in enumerate(id2word)}
```

Only extract embeddings for words that exist in your existing vocabulary.

```py
embeddings_file = '/home/ronny/TEMP/gloVe/glove.6B/glove.6B.100d.txt'
embedding_size = 100

n_vocab = len(id2word)
embeddings = np.zeros([n_vocab, embedding_size], dtype=np.float32)
count = 0
with open(embeddings_file, "r") as fileobj:
    for line in fileobj:
        line = line.split()
        word, vector = line[0], np.array(line[1:], dtype=np.float32)
        if word in word2id:
            count += 1
            embeddings[word2id[word]] = vector

# Show a message if there are words that do not have embeddings
if count < n_vocab:
    print("Not all words in vocab could be located in embeddings file")
```


## Playing around with word vectors

Similarity between words

```py
def cosine_similarity(a,b):
    """ Cosine Similarity between two vectors"""
    return np.dot(a,b) / (np.linalg.norm(a, 2)*np.linalg.norm(b, 2))

def cosine_similarity_words(a, b):
    """ Given word strings, it finds the cosine similarity of the two
        word vectors that represent those words"""
    return cosine_similarity(embeddings[word2id[a]], embeddings[word2id[b]])

cosine_similarity_words("woman", "man") # 0.83234936
cosine_similarity_words("king", "queen") # 0.75076908
cosine_similarity_words("king", "lizard") # 0.23220986
```

Word vector arithmetic

```py
y = embeddings[word2id["king"]] - embeddings[word2id["man"]] + embeddings[word2id["woman"]]

queen = embeddings[word2id["queen"]]
lizard = embeddings[word2id["lizard"]]
cosine_similarity(y,queen) # 0.78344142
cosine_similarity(y,lizard) # 0.18114193
```