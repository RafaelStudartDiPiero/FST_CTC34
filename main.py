import networkx as nx
import matplotlib.pyplot as plt
from fst.fst import read_input_fst, auto_complete_fst, read_fst
from trie.trie import read_input_trie, auto_complete_trie, read_trie

if __name__ == "__main__":
    fst = read_fst()
    print(read_input_fst("ma", fst))
    print(auto_complete_fst('ma', fst))

    trie = read_trie()
    print(read_input_trie("ma", trie))
    print(auto_complete_trie("ma", trie))


# pos = nx.shell_layout(fst)
# plt.figure(figsize=(20, 20))
# nx.draw(fst, pos, with_labels=True)
# nx.draw_networkx_edge_labels(fst, pos)
# plt.savefig("fst.png")

# pos = nx.shell_layout(trie)
# plt.figure(figsize=(20,20))
# nx.draw(trie, pos, with_labels=True)
# nx.draw_networkx_edge_labels(trie, pos)
# plt.savefig("trie.png")
