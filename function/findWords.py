import re, random, os

def searchWords(letters):
    # Get the directory path of the current script
    scriptDir = os.path.dirname(__file__)
    
    # Construct the path to words.txt relative to the current script
    wordPath = os.path.join(scriptDir, '..', 'static', 'words.txt')
    
    with open(wordPath, 'r') as file:
        words = [word.strip() for word in file]

    pattern = re.compile('.*' + letters + '.*', re.IGNORECASE)
    matchingWords = [word for word in words if pattern.match(word)]
    matchingWords = sorted(matchingWords, key=len)

    if len(matchingWords) == 0:
        pass
    else:
        newWords = []
        for i in range(10):
            num = random.randint(0, len(matchingWords) - 1)
            newWords.append(matchingWords[num])

        newWords = sorted(newWords, key=len)

        print("Words containing '{}' are: {}".format(letters, newWords))
        return newWords