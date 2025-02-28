import os
import math
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpusroot = './US_Inaugural_Addresses'
documents = {}
tokens_freq = {}  # Term frequency per document
doc_freq = {}     # Document frequency per token
tfidf_vectors = {}  # Normalized TF-IDF vectors
postings = {}     # Postings lists for each token
N = 0             # Total number of documents
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'[a-zA-Z]+') 

# Preprocess the corpus
def preprocess_corpus():
    global N
    for filename in os.listdir(corpusroot):
        if filename.endswith('.txt'):
            with open(os.path.join(corpusroot, filename), 'r', encoding='windows-1252') as file:
                text = file.read().lower()  # Convert text to lowercase
                tokens = tokenizer.tokenize(text)  # Tokenize text
                tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
                documents[filename] = tokens
                # term frequency
                tokens_freq[filename] = {}
                for token in tokens:
                    tokens_freq[filename][token] = tokens_freq[filename].get(token, 0) + 1
                # document frequency
                for token in set(tokens):
                    doc_freq[token] = doc_freq.get(token, 0) + 1
    N = len(documents)

# TF-IDF vectors and postings lists
def compute_tfidf():
    for filename, tokens in documents.items():
        tfidf_vectors[filename] = {}
        # Compute TF-IDF weights
        for token in set(tokens):
            tf = 1 + math.log10(tokens_freq[filename][token])
            idf = math.log10(N / doc_freq[token])
            tfidf_vectors[filename][token] = tf * idf
        # Normalize the vector
        norm = math.sqrt(sum(w ** 2 for w in tfidf_vectors[filename].values()))
        if norm > 0:
            for token in tfidf_vectors[filename]:
                tfidf_vectors[filename][token] /= norm
        # Build postings lists
        for token in tfidf_vectors[filename]:
            if token not in postings:
                postings[token] = []
            postings[token].append((filename, tfidf_vectors[filename][token]))
    # Sort postings lists by weight
    for token in postings:
        postings[token].sort(key=lambda x: x[1], reverse=True)

# IDF for a token
def getidf(token):
    token = stemmer.stem(token.lower())  # Ensure lowercase input
    if token not in doc_freq:
        return -1
    return math.log10(N / doc_freq[token])

# TF-IDF weight for a token in a document
def getweight(filename, token):
    token = stemmer.stem(token.lower())  # Ensure lowercase input
    return tfidf_vectors.get(filename, {}).get(token, 0)

# compute its TF-IDF vector
def process_query(qstring):
    tokens = tokenizer.tokenize(qstring.lower())  # Convert query to lowercase
    tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    if not tokens:
        return None, 0
    tf = {}
    query_vector = {}
    # term frequency in query
    for token in tokens:
        tf[token] = tf.get(token, 0) + 1
    # TF-IDF weights
    for token in set(tokens):
        if token in doc_freq:
            tfidf = (1 + math.log10(tf[token])) * math.log10(N / doc_freq[token])
            query_vector[token] = tfidf
    # Normalize query vector
    norm = math.sqrt(sum(w ** 2 for w in query_vector.values()))
    for token in query_vector:
        query_vector[token] /= norm
    return query_vector, tokens

#compute cosine similarity 
def query(qstring):
    query_vector, query_tokens = process_query(qstring)
    if not query_vector:
        return "None", 0  # No valid terms in query

    candidates = {}
    for token in query_tokens:
        if token in postings:
            for doc, weight in postings[token]:
                if doc not in candidates:
                    candidates[doc] = 0
                candidates[doc] += query_vector[token] * weight  # Compute cosine similarity

    if not candidates:  
        return "fetch more", 0.0

    
    best_doc = max(candidates, key=candidates.get)
    best_score = candidates[best_doc]

    return best_doc, best_score


preprocess_corpus()
compute_tfidf()


if __name__ == "__main__":
    print("%.12f" % getidf('british'))
    print("%.12f" % getidf('union'))
    print("%.12f" % getidf('dollar'))
    print("%.12f" % getidf('constitution'))
    print("%.12f" % getidf('power'))
    print("--------------")
    print("%.12f" % getweight('19_lincoln_1861.txt', 'states'))
    print("%.12f" % getweight('07_madison_1813.txt', 'war'))
    print("%.12f" % getweight('05_jefferson_1805.txt', 'false'))
    print("%.12f" % getweight('22_grant_1873.txt', 'proposition'))
    print("%.12f" % getweight('16_taylor_1849.txt', 'duties'))
    print("--------------")
    print("(%s, %.12f)" % query("executive power"))
    print("(%s, %.12f)" % query("foreign government"))
    print("(%s, %.12f)" % query("public rights"))
    print("(%s, %.12f)" % query("people government"))
    print("(%s, %.12f)" % query("states laws"))