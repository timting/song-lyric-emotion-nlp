#!/usr/bin/env python

import argparse
import csv
from keras import *
import numpy as np

def get_model(input_shape, num_classes):
    model = Sequential()
    model.add(layers.Conv1D(32, kernel_size=(5), strides=(1),
                            activation='relu',
                            input_shape=input_shape))
    model.add(layers.MaxPooling1D(pool_size=(2), strides=(2)))
    model.add(layers.Conv1D(64, (5), activation='relu'))
    model.add(layers.MaxPooling1D(pool_size=(2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(1000, activation='relu'))
    model.add(layers.Dense(num_classes, activation='softmax'))

    return model

def main():
    parser = argparse.ArgumentParser(description="emotions multi-classifier trianer")
    parser.add_argument("--input INPUT", type=str, help="Input csv file")
    parser.add_argument("--output OUTPUT", type=str, help="Output model file")
    args = parser.parse_args()

    training_data = []
    training_labels = []

    labels = set()

    rows = 0
    with open(args.input) as input_file:
        reader = csv.reader(input_file, delimiter='|')
        for row in reader:
            rowlist = list(row)
            label = rowlist.pop()
            training_data.append(rowlist)
            training_labels.append(label)
            labels.add(label)
            rows += 1

    num_features = len(training_labels[0])
    num_classes = len(labels)

    model = get_model((num_features, rows), num_classes)
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train
    model.fit(training_data, training_labels, epochs=10, batch_size=32)

    model.save(args.output)

    return

if __name__ == "__main__":
    main()
