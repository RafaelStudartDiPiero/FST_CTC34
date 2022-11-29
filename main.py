import networkx as nx
import matplotlib.pyplot as plt
from fst.fst import create_minimal_transducer, read_input_fst, auto_complete_fst
from trie.trie import create_trie, read_input_trie, auto_complete_trie


def create_dictionary():
    dictionary = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
                  "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
    dictionary = dict(sorted(dictionary.items()))
    return dictionary


dictionary = create_dictionary()
fst = create_minimal_transducer(dictionary)
# pos = nx.shell_layout(fst)
# plt.figure(figsize=(20, 20))
# nx.draw(fst, pos, with_labels=True)
# nx.draw_networkx_edge_labels(fst, pos)
# plt.savefig("fst.png")
print(read_input_fst("mat", fst))
print(auto_complete_fst('ma', fst))

trie = create_trie(dictionary)
# pos = nx.shell_layout(trie)
# plt.figure(figsize=(20,20))
# nx.draw(trie, pos, with_labels=True)
# nx.draw_networkx_edge_labels(trie, pos)
# plt.savefig("trie.png")
print(read_input_trie("mat", trie))
print(auto_complete_trie("may", trie))
