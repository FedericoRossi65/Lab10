from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        self.G.clear()
        self._edges = []

        all_tratte = DAO.get_tratta()
        hubs = {h.id: h.nome for h in DAO.get_hub()}

        for t in all_tratte:
            peso = t.peso_tratta()
            if peso >= threshold:
                self.G.add_edge(t.h1, t.h2, weight=peso)

                # salva la stringa coi nomi, NON fare query
                nome_tratta = f"{hubs[t.h1]} --> {hubs[t.h2]}"
                self._edges.append((nome_tratta, peso))

        return self.G

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """

        return len(self._edges)

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """

        return len(DAO.get_hub()) # mi restituisce tutti gli hub esistenti

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """

        return self._edges




