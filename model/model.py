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
        #il grafo è stato inzializzato nel costruttore adesso sara popolato da nodi(hub) e archi (le tratte) con peso Tratta.peso_tratta
        self._nodes = []
        self._edges = []
        self.G.clear()
        self._nodes = DAO.get_hub()
        self._edges = DAO.get_tratta()
        self.G.add_nodes_from(self._nodes)
        tratte_totali = DAO.get_tratta()
        for t in tratte_totali:
            if t.peso_tratta() >= threshold:
                u = t.hub_partenza
                v = t.hub_arrivo
                peso = t.peso_tratta()

                # Aggiungo l'arco tra u e v con il peso specificato
                self.G.add_edge(u, v, weight=peso)
        return self.G







    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        num_edges = self.G.number_of_edges()
        return num_edges

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        num_nodi = self.G.number_of_nodes()
        return num_nodi

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        for u, v,data in self.G.edges(data=True):
            peso = data['weight']
            # Restituisco la tripla pulita
            yield u, v, peso




