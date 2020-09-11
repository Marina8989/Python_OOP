"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary"""
    def __init__(self, path):
        """Read dictionary and reposrts # items read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Return random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
        """Specialized WordFinder that excludes blank lines/comments"""
        def parse(self, dict_file):
            """parse dict_file -> list of words, skipping blanks/comments"""
            return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]
