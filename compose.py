import random
import re
import string
from os import listdir
from os.path import isfile

from graph import Graph


class MCTextComposer:
    def __init__(self, path: str):
        self._markov_graph = Graph()
        self._words = None
        self._generate_graph_recursive(path)

    def _read_text(self, path: str):
        with open(path) as f:
            text = f.read()
            text = re.sub(r'\[(.+)]', ' ', text)
            self._words = ' '.join(text.split()).translate(
                str.maketrans('', '', string.punctuation.replace('\'', ''))).lower().split()

    def _generate_graph(self, words):
        prev_vertex = None
        for word in words:
            current_vertex = self._markov_graph.get_vertex(word)
            if prev_vertex:
                prev_vertex.increment_edge(current_vertex)
            prev_vertex = current_vertex

    def _compose(self, word, length):
        composition = []
        current_word = self._markov_graph.get_vertex(word)
        for _ in range(length):
            composition.append(current_word.value)
            current_word = self._markov_graph.get_next_word(current_word)
        return ' '.join(composition)

    def _generate_graph_recursive(self, path: str):
        if isfile(path):
            self._read_text(path)
            self._generate_graph(self._words)
            return
        file_names = listdir(path)
        for file_name in file_names:
            self._generate_graph_recursive(path + '/' + file_name)

    def generate_new_graph(self, path: str):
        self._markov_graph.flush()
        self._generate_graph_recursive(path)

    def compose_random_chain(self, length: int = 50):
        return self._compose(random.choice(self._words), length)

    def compose_chain_from(self, word: str, length: int = 50):
        if word not in self._markov_graph.get_vertex_values():
            return self.compose_random_chain(length)
        return self._compose(word, length)
