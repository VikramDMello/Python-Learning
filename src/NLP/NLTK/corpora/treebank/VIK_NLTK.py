import os
import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk import chunk
from nltk import ne_chunk
from nltk import parse_sents
from nltk.corpus import treebank
from nltk.tree import Tree

os.system('clear')

with open('/Users/vix/nltk_data/corpora/treebank/raw/VIK_NLTK.txt') as rawtextfile:
    sentence_orig = rawtextfile.read()
    # sentence = "The dog chased the cat."
    print("\nOriginal sentence: \n\t"+ str(sentence_orig))
    
tokens = nltk.word_tokenize(sentence_orig)
print("\nTokens: \n\t" + str(tokens))

tags = nltk.pos_tag(tokens)
print("\nTags: \n\t" + str(tags))

sentence_tree1 = list(map(lambda sent: Tree(sent[1], children=[sent[0]]), tags))

pattern = """NP: {<DT>?<JJ>*<NN>}
VBD: {<VBD>}
IN: {<IN>}"""
NPChunker = nltk.RegexpParser(pattern) 
sentence_tree2 = NPChunker.parse(sentence_tree1)

sentence_tree2.draw()


# sentence_tree2 = nltk.ne_chunk(sentence_tree1)

# print("\nFlat Tree: \n\t" + str(tree_flat))

# tree = treebank.parsed_sents('VIK_NLTK.mrg')[0]
# print(tree)
# tree.draw()


# sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]

# from nltk.stem.porter import PorterStemmer
# stemmer = PorterStemmer()

# words = ['As', 'the', 'drizzle', '--', 'and', 'the', 'tears', 'and', 'the', 'lies', '--', 'came', 'gradually', 'to', 'a', 'halt', ',', 'they', 'clasped', 'hands', ';', 'with', 'an', 'end-of-the-world', 'look', 'in', 'his', 'eyes', ',', 'Patrice', 'whispered', ',', '``', 'The', 'King', 'of', 'Belgium', "'s", 'private', 'secretary', 'was', 'here', 'and', 'he', 'said', ',', "'remember", 'this', ',', 'when', 'in', 'Paris', ':', 'Kasai', ',', 'Kasai', '!', "'", "''"]

# for word in words:
#     print("\n" + word + "\n\t" + stemmer.stem(word))




# nltk.draw.tree.demo()
# nltk.draw.tree.draw_trees(tree_flat)

# grammar = "NP: {<DT>?<JJ>*<NN>}"
# chunkparser = nltk.RegexpParser(grammar)

# sentencetree = chunkparser.parse(tags)

# tree_flat.pretty_print()

# with open('/Users/vix/nltk_data/corpora/treebank/combined/VIK_NLTK.mrg', 'w') as treefile:
#     sentencetree = treefile.write(str(entities))
    

# t.draw()

# from nltk import pos_tag_sents
# from nltk import ne_chunk
# # from nltk import TreebankWordTokenizer
# from nltk import parse
# from nltk import treebank
# from nltk import parse
# from nltk import corpus
# from nltk download('words')
