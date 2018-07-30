import csv

# This script creates binary features for the isear dataset

features = []

emotions_to_int = {
    "joy": 0,
    "fear": 1,
    "anger": 2,
    "sadness": 3,
    "disgust": 4,
    "shame": 5,
    "guilt": 6
}

with open('grams.txt') as columns:
    readFeatures = csv.reader(columns)
    for row in readFeatures:
        features.append(row[0])

with open('isear-noa.csv') as rows:
    readCSV = csv.reader(rows, delimiter='|',
                                  quotechar='"')

    with open('features.csv', 'w+') as output:
        writer = csv.writer(output, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for idx, row in enumerate(readCSV):
            if idx == 0:
                result_row = features
                result_row.append("Label")
            else:
                text = row[-3]
                label = row[36]
                result_row = [0 if feature not in text else 1 for feature in features]
                result_row.append(emotions_to_int[label])

            writer.writerow(result_row)