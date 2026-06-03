"""
    This module contains the Index class, which is responsible for managing an index.
"""
class Index:
    def __init__(self, index):
        self.index = index

    def search(self, query):
        return self.index.get(query, [])