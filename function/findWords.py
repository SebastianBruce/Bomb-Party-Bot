import re, random, os

def searchWords(letters):
    # Get the directory path of the current script
    scriptDir = os.path.dirname(__file__)
    
    # Construct the path to words.txt relative to the current script
    wordPath = os.path.join(scriptDir, '..', 'static', 'words.txt')
    
    # Open words.txt and extract words into a list
    with open(wordPath, 'r') as file:
        words = [word.strip() for word in file]

    # Create a regex pattern to match words containing specified letters
    pattern = re.compile('.*' + letters + '.*', re.IGNORECASE)
    
    # Filter words matching the pattern
    matchingWords = [word for word in words if pattern.match(word)]
    
    # Sort matching words by length
    matchingWords = sorted(matchingWords, key=len)

    # If no matching words found, return None
    if len(matchingWords) != 0:
        # Randomly select 10 matching words
        if len(matchingWords) >= 10:
            newWords = random.sample(matchingWords, 10)
        else:
            newWords = matchingWords
        
        # Sort selected words by length
        newWords = sorted(newWords, key=len)

        # Print and return the selected words
        print("Words containing '{}' are: {}".format(letters, newWords))
        return newWords
