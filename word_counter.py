#Purva Patel #100886734
from collections import Counter
import string

# Defining a class to count the occurrence of words in a file
class WordCounter:
    # Initializing the class with the file name
    def __init__(self, file):
        self.file = file
        self.words_dict = self.get_words_dict()

    # Defining a function to get a dictionary with word counts
    def get_words_dict(self):
        # Opening the file and reading its contents
        with open(self.file) as f:
            Words = f.read().split()
        # Removing punctuation from each word
        Words = [w.strip(string.punctuation) for w in Words]
        # Counting the occurrence of each word using Counter
        words_dict = Counter(Words)
        return words_dict

    # Defining a function to print the top 10 words
    def top_10_words(self):
        # Using most_common() function of Counter to get top 10 words
        topletters = self.words_dict.most_common(10)    
        for x, word in enumerate(topletters):
            print(f"{x}: ('{word[0]}', {word[1]})")


# Defining the main function to execute the code
def main():
    # Creating an instance of WordCounter class with the file name
    countLetters = WordCounter('text.txt')
    # Calling top_10_words() function to print top 10 words
    countLetters.top_10_words()


# Checking if the code is being run as the main program
if __name__ == '__main__':
    # Calling the main function to execute the code
    main()
