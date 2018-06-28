import spacy
import csv
import textacy

nlp = spacy.load('en')

total_string = ""

with open('isear-noa.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='|',
                                  quotechar='"')

    index = 0
    for row in readCSV:
        total_string = total_string + " " + row[-3]
        index = index + 1

#print(total_string)

doc = nlp(total_string)
print(list(textacy.extract.ngrams(doc, 2, filter_stops=True, filter_punct=True, filter_nums=False))[:15])


