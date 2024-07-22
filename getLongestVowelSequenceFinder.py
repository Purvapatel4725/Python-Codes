def isVowel(string):
    if string in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

def getLongestVowelSequence(string):
    longestVowelInWord = ""
    currentVowelInword = ""
    for i in string:
        if isVowel(i):
            currentVowelInword = currentVowelInword + i
            if len(currentVowelInword) > len(longestVowelInWord):
                longestVowelInWord = currentVowelInword
        else:
            currentVowelInword = ""
    return longestVowelInWord

getLongestVowelSequence("Hooiaioia is a cool word in Hawaiian") 
getLongestVowelSequence("Queuing is not quite as impressive") 