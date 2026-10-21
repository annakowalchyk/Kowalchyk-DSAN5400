import xml.etree.ElementTree as ET
from nltk.tokenize import word_tokenize
import string
from nltk.stem import PorterStemmer
from collections import Counter
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", type=str, required=True)
parser.add_argument("-t", "--tokenizer", type=str, required=True)
parser.add_argument("-s", "--stem", type=str, required=True)

args = parser.parse_args()

# Read in file
# initial = ET.parse('20newsgroups-initial.xml')
# additional = ET.parse('20newsgroups-additional.xml')
fp = ET.parse(args.file)
# Get root element
root_initial = fp.getroot()

# Store list of documents
documents = {}

# element.tag -> doc_id and msgtext
# element.text -> doc_id number and text
for child in root_initial:
    docid = child.find('docid').text
    msg = child.find('msgtext').text
    documents[docid] = msg

# Get root element
# root_initial = additional.getroot()

# for child in root_initial:
#    docid = child.find('docid').text
#    msg = child.find('msgtext').text
#    documents[docid] = msg

# print(documents)

# Tokenizer interface
class Tokenizer:
    """Tokenizer interface"""

    def __init__(self, text):
        self.text = text

    def tokenize(self):
        """ Split text based on directions
        Args:
            none

        Returns:
            list of tokens
        """
        pass

    def normalize(self, tokens):
        """ Normalize tokens by lowercasing and removing punctuation
        Args:
            list of tokens

        Returns:
            list of normalized tokens
        """
        for i in range(0, len(tokens)):
            tokens[i] = tokens[i].lower().strip(string.punctuation)

        return tokens

    def stem(self, tokens):
        stems = []
        # Stemmer instance
        ps = PorterStemmer()
        for token in tokens:
            stems.append(ps.stem(token))
        return stems


class WhitespaceTokenizer(Tokenizer):

    def __init__(self, text):
        self.text = text

    def tokenize(self):
        tokens = self.text.split(maxsplit = -1)
        return tokens



class OffshelfTokenizer(Tokenizer):
    def __init__(self, text):
        self.text = text
    
    def tokenize(self):
        tokens = word_tokenize(self.text)
        return tokens
    

class NTokenizer(Tokenizer):
    def __init__(self, text, ngram = 4):
        self.text = text
        self.ngram = ngram

    def tokenize(self):
            tokens = []
            for character in range(0, len(self.text) - self.ngram + 1):
                tokens.append(self.text[character : character+self.ngram])
            return tokens

    def get_docs(self, token):
        found_docs = None
        tk = NTokenizer(token)
        tokens = tk.normalize(tk.tokenize())
        if args.stem == 'True':
            tokens = tk.stem(tokens)
        for token in tokens:
            doc_ids = {docid for docid, freq in ngram_index.get(token, [])}
            if found_docs is None:
                found_docs = doc_ids
            else:
                found_docs = found_docs.intersection(doc_ids)

        return list(found_docs)

# Hardcode Search Words
if args.stem == 'True':
    stemmer = PorterStemmer()
    system_search = stemmer.stem('system')
    search = stemmer.stem('compatibility')
else:
    system_search = 'system'
    search = 'compatibility'

# WHITESPACE
if args.tokenizer == 'whitespace':
    ws_index = {}
    for docid, text_body in documents.items():
        # instance of class
        tk = WhitespaceTokenizer(text_body)
        list_of_tokens = tk.tokenize()
        normal_tokens = tk.normalize(list_of_tokens)
        if args.stem == 'True':
            normal_tokens = tk.stem(normal_tokens)
        term_frequency = Counter(normal_tokens)
        for token in term_frequency:
            if token in ws_index:
                ws_index[token] += [(docid, term_frequency[token])]
            else:
                ws_index[token] = [(docid, term_frequency[token])]

    print("----------SYSTEM SEARCH----------")
    print(f"Whitespace Tokenizer: {[doc_id for doc_id, count in ws_index.get(system_search)]}")
    print("----------COMPATIBILITY SEARCH----------")
    print(f"Whitespace Tokenizer: {[doc_id for doc_id, count in ws_index.get(search)]}")
    ws_sys = set([doc_id for doc_id, count in ws_index.get(system_search)])
    ws_comp = set([doc_id for doc_id, count in ws_index.get(search)])
    print("----------SYSTEM AND COMPATIBILITY SEARCH----------")
    print(f"Whitespace Tokenizer: {ws_sys & ws_comp}")
    

# OFF SHELF
elif args.tokenizer == 'off':
    off_index = {}
    for docid, text_body in documents.items():
        # instance of class
        tk = OffshelfTokenizer(text_body)
        list_of_tokens = tk.tokenize()
        normal_tokens = tk.normalize(list_of_tokens)
        if args.stem == 'True':
            normal_tokens = tk.stem(normal_tokens)
        term_frequency = Counter(normal_tokens)
        for token in term_frequency:
            if token in off_index:
                off_index[token] += [(docid, term_frequency[token])]
            else:
                off_index[token] = [(docid, term_frequency[token])]

    print("----------SYSTEM SEARCH----------")
    print(f"Off the Shelf Tokenizer: {[doc_id for doc_id, count in off_index.get(system_search)]}")
    print("----------COMPATIBILITY SEARCH----------")
    print(f"Off the Shelf Tokenizer: {[doc_id for doc_id, count in off_index.get(search)]}")
    # Off the Shelf
    print("----------SYSTEM AND COMPATIBILITY SEARCH----------")
    off_sys = set([doc_id for doc_id, count in off_index.get(system_search)])
    off_comp = set([doc_id for doc_id, count in off_index.get(search)])
    print(f"Off the Shelf Tokenizer: {off_sys & off_comp}")

elif args.tokenizer == 'ngram':
    # ngram
    ngram_index = {}
    for docid, text_body in documents.items():
        # instance of class
        tk = NTokenizer(text_body)
        list_of_tokens = tk.tokenize()
        normal_tokens = tk.normalize(list_of_tokens)
        if args.stem == 'True':
            normal_tokens = tk.stem(normal_tokens)
        term_frequency = Counter(normal_tokens)
        for token in term_frequency:
            if token in ngram_index:
                ngram_index[token] += [(docid, term_frequency[token])]
            else:
                ngram_index[token] = [(docid, term_frequency[token])]
    
    print("----------SYSTEM SEARCH----------")
    print(f"N-Gram Tokenizer: {tk.get_docs("system")}")
    # COMPATIBILITY SEARCH
    print("----------COMPATIBILITY SEARCH----------")
    print(f"N-Gram Tokenizer: {tk.get_docs("compatibility")}")
    # SYSTEM AND COMPATIBILITY SEARCH
    print("----------SYSTEM AND COMPATIBILITY SEARCH----------")
    # N-Gram
    n_sys = set(tk.get_docs("system"))
    n_comp = set(tk.get_docs("compatibility"))
    print(f"N-Gram Tokenizer: {n_sys & n_comp}")


