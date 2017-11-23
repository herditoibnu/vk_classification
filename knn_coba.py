import csv
import random
import math
import operator
import pandas as pd


#modified from: https://github.com/MarioPerezEsteso/k-Nearest-Neighbors-in-Python/blob/master/irisknn.py


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def getResponse(neighbors):
    # Creating a list with all the possible neighbors
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


def main():
    trainingSet = pd.read_csv('pixeldikit_train.csv', header=None)
    trainingSet = trainingSet.values.tolist()

    testSet = pd.read_csv('pixeldikit_test.csv', header=None)
    testSet = testSet.values.tolist()

    print 'Train set: ' + str(len(trainingSet))
    print 'Test set: ' + str(len(testSet))
    predictions = []
    k = 3
    for x in range(len(testSet)):
        # print "gambar ke: " + str(x+1)
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        # print('> predicted=' + str(result) + ', actual=' + str(testSet[x][-1]))

    accuracy = getAccuracy(testSet, predictions)
    print 'Accuracy: ', accuracy


main()