from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path_to_file):
        """Initializes WordFinder instance"""

        self.generateListOfWords(path_to_file)
        self.words = self.cleanUpNewLines()

    def __repr__(self):
        """Represents what attributes this instance of WordFinder has"""

        return (
            f"<WordFinder words = {self.words}"
        )

    def cleanUpNewLines(self):
        """Removes newline char '\n' from word"""

        list_without_newlines = []
        for word in self.words:
            if word.endswith('\n'):
                print('We got into here because it has newline', word)
                new_word = word.replace('\n', '')
                print('This is the new word, did it remove?', word)
                list_without_newlines.append(new_word)
            else:
                list_without_newlines.append(word)
        print('This is list_without_newlines before return', list_without_newlines)
        return list_without_newlines

    def random(self):
        """Chooses a random word from list of words"""

        picked_word = choice(self.words)
        return picked_word

    def generateListOfWords(self, path_to_file):
        """Takes in a file; returns a list of words"""

        self.words = []
        file = open(path_to_file)
        for word in file:
            # word.strip()
            self.words.append(word)
        print(f"{len(self.words)} words read")
        file.close()
