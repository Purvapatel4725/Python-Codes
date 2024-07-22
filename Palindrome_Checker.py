def functionToFindIfTheWordIsPalindrom(word):
    reversedWord = word[::-1]
    if reversedWord == word:
        return True
    else:
        return False

print(functionToFindIfTheWordIsPalindrom("aibohphobia"))

