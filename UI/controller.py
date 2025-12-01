import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """

        self._view.lista_visualizzazione.controls.clear()
        soglia = float(self._view.guadagno_medio_minimo.value)
        self._model.costruisci_grafo(soglia)
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Hub: {self._model.get_num_nodes()}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Tratte: {self._model.get_num_edges()}"))
        lista_tratte = self._model.get_all_edges()
        for oggetto in lista_tratte:

            self._view.lista_visualizzazione.controls.append(ft.Text(f"{oggetto[0]} --> Guadagno medio per spedizione: {oggetto[1]}"))


        self._view.update()


