__author__ = "Tom Sherman"
__version__ = "1.0"

"""
    This script reads from a file (dictionary.txt), generates a hashmap (dict) and dumps it to a json file.
    Only needs to be run once, unless the dictionary changes.

    It's quite slow, but once completed lookup of valid matches is blazing fast.
"""

import collections
import json


dictFileName = "dictionary.txt"
mapFileName = "map.json"


def createdict(filename):
    """
        Reads a txt file of words, one word per line, and stores that in a map (dict).

        Keys are unique signatures of one or more words - an ordered list of letters
        that can make up each word in the dictionary. The values are the words the
        signature can make.

    :return dmap:
    :param filename: A text file, one word per line
    """
    # the "signature" of a word is the ordered list of its letters

    dictfile = open(filename)                      # open the wordlist
    dmap = collections.defaultdict(list)       # associate to each signature the words that have that signature
    signatures = []                         # store here all the signatures to count them

    for x in dictfile.readlines():
        signature = "".join(sorted(x.strip()))  # get the word signature

        signatures.append(signature)
        dmap[signature].append(x.strip())
    dictfile.close()

    return dmap


def storejson(dmap):
    """
        Stores the map as a json txt file.

        :param dmap:
    """

    jsoncontent = json.dumps(dmap)

    with open(mapFileName, "w") as f:
        f.write(jsoncontent)


def readjson(filename):
    """
        Reads a json file and returns it as a dict (map)
    :param filename:
    :return json dict:
    """
    with open(filename) as f:
        return json.loads(f.read())


if __name__ == '__main__':
    dictmap = createdict(dictFileName)
    storejson(dictmap)
    print("JSON file generated from " + dictFileName)
