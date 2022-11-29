import networkx as nx
from trie.trie import create_trie
from dictionary import create_dictionary

if __name__ == "__main__":
    dictionary = create_dictionary()
    trie = create_trie(dictionary)
    nx.write_gpickle(trie, "generated_trie")
