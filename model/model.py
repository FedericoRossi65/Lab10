from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """



        self.G.clear()
        self._nodes = []
        self._edges = [] # Questa lista conterrà le 31 tratte

        all_tratte = DAO.get_tratta()



        for t in all_tratte:
            if t.peso_tratta() >= threshold:
                u = t.h1
                v = t.h2
                peso = t.peso_tratta()

                # Aggiungo all'arco (Il grafo ne conterrà 29 alla fine)
                self.G.add_edge(u, v, weight=peso)

                # Aggiungo alla lista (La lista ne conterrà 31)
                self._edges.append((t,peso))


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




