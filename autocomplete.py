#! python
import time
from trienode import TrieNode

dictionary=[]
t = None


def autocomplete(words=[], term='', amount=1):
    result=[]
    words = sort(words) # O(Nlog(N))

    for word in words: # O(N)
        if word.startswith(term): # O(M)
            result.append(word)
        if len(result) == amount:
            break
    return result


def autocomplete2(words=[], term='', amount=1):
    result=[]
    words = sort(words) # O(Nlog(N))

    for word in words: # O(N) ---Improve by using binary search turns into log(N)
        if word.startswith(term): # O(M)
            result.append(word)
        if len(result) == amount:
            break
    return result

def binary_search_prefix():
    middle = abs(len(words) / 2)

def get_words(filename='/usr/share/dict/words', amount_of_lines=100):
    if len(dictionary) is not 0:
        return
    counter = 0
    with open(filename) as f:
        for line in f:
            line = line.lower()
            counter += 1
            dictionary.append(line[:-2])

def put_dictionary():
    t = TrieNode("", True);
    t.append_all(dictionary)
    return t

def autocomplete(t, prefix="appear"):
    prefix = prefix.lower()
    # print(t.table)
    millis = time.time()
    print(t.get(prefix, True))
    millis2 = time.time()
    print(millis2 - millis)

if __name__ == "__main__":
    get_words()
    t = put_dictionary()
    autocomplete(t)
