# This file creats unigrams and bigrams from the ISEAR dataset and outputs them
# to grams.txt

import spacy
import csv
import textacy

nlp = spacy.load('en')

all_sentences = []

# Pull in csv file, each passage
with open('isear-noa.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='|',
                                  quotechar='"')

    index = 0
    for row in readCSV:
        all_sentences.append(row[-3])
        index = index + 1

# Find uni/bi-grams in each passage
docs = [nlp(s) for s in all_sentences]
unigrams = [list(textacy.extract.ngrams(d, 1, filter_stops=True, filter_punct=True, filter_nums=True)) for d in docs]
unigrams = set([item.text for sublist in unigrams for item in sublist])
bigrams = [list(textacy.extract.ngrams(d, 2, filter_stops=True, filter_punct=True, filter_nums=True)) for d in docs]
bigrams = set([item.text for sublist in bigrams for item in sublist])

# Write uni/bi-grams, carriage return separated, into grams.txt
with open('grams.txt', 'w+') as f:
    f.write('\n'.join(unigrams))
    f.write('\n')
    f.write('\n'.join(bigrams))

