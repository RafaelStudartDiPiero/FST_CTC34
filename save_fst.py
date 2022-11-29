import networkx as nx
from fst.fst import create_minimal_transducer
from dictionary import create_dictionary

if __name__ == "__main__":
    dictionary = create_dictionary()
    fst = create_minimal_transducer(dictionary)
    nx.write_gpickle(fst, "generated_fst")
