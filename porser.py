import nltk
from nltk import pos_tag
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_noun_phrases(sentence):
    words = word_tokenize(sentence)
    
    tagged_words = pos_tag(words)
    
    grammar = 'NP: {<DT>?<JJ>*<NN.*>+}'
    
    chunk_parser = RegexpParser(grammar)
    
    tree = chunk_parser.parse(tagged_words)
    
    noun_phrases = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            noun_phrase = " ".join(word for word, tag in subtree.leaves())
            noun_phrases.append(noun_phrase)
    
    return noun_phrases

sentence = "The quick brown fox jumps over the lazy dog."
noun_phrases = extract_noun_phrases(sentence)
print("Noun Phrases:", noun_phrases)