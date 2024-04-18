import sys


def max_match(sentence, dictionary):
    if not sentence:
        return []
    
    for i in range(len(sentence), 0, -1):
        firstword = sentence[:i]
        remainder = sentence[i:]
        if firstword in dictionary:
            return [firstword] + max_match(remainder, dictionary)
    
    # No word was found, so make a one-character word and check the remainder
    firstword = sentence[0]
    remainder = sentence[1:]
    if remainder and remainder[:1] in dictionary:
        return [firstword + remainder[:1]] + max_match(remainder[1:], dictionary)
    else:
        return [firstword] + max_match(remainder, dictionary)

if __name__ == "__main__":
    
    with open(sys.argv[1], 'r', encoding='utf-8') as dfile:
        dictionary = set(dfile.read().splitlines())

    # The sentences are read from stdin
    for line in sys.stdin:
        sentence = line.strip()
        segmentation = max_match(sentence, dictionary)
        print(' '.join(segmentation))