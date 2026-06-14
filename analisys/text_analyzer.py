"""
    This module contains the TextAnalyzer class, which is responsible for analyzing text and
    extracting patterns.
"""


class TextAnalyzer:
    def __init__(self):
        self.texts = []

    def add_text(self, text):
        self.texts.append(text)

    def get_patterns(self):
        patterns = {}
        for text in self.texts:
            words = text.split()
            for word in words:
                patterns[word] = patterns.get(word, 0) + 1
        return patterns

    def brute_force_search(self, text, pattern):
        """
        Find all starting indices where `pattern` appears in `text` using
        brute-force string matching. Returns a list of indices.
        Complexity: O(n*m), where n = len(text), m = len(pattern).
        """
        if not pattern:
            return []
        n, m = len(text), len(pattern)
        matches = []
        for i in range(n - m + 1):
            j = 0
            while j < m and text[i + j] == pattern[j]:
                j += 1
            if j == m:
                matches.append(i)
        return matches

    def _build_lps(self, pattern):
        """
        Build the Longest Prefix Suffix (LPS) table for KMP.
        lps[i] = length of the longest proper prefix of pattern[0..i]
                that is also a suffix.
        Complexity: O(m).
        """
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def kmp_search(self, text, pattern):
        """
        Find all starting indices where `pattern` appears in `text` using
        Knuth-Morris-Pratt algorithm. Returns a list of indices.
        Complexity: O(n + m).
        """
        if not pattern:
            return []
        n, m = len(text), len(pattern)
        lps = self._build_lps(pattern)
        matches = []
        i = j = 0
        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == m:
                    matches.append(i - j)
                    j = lps[j - 1]
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return matches
