import nltk
import numpy
import tflearn
import tensorflow
import json

import pickle
import gensim
from pyvi import ViTokenizer
from const.Constant import *


class TrainingService:
    def __init__(self, modelName):
        self.modelName = modelName

        with open("data/" + self.modelName + ".json", encoding="utf-8") as file:
            data = json.load(file)

        try:
            with open("data/" + self.modelName + ".pickle", "rb") as f:
                words, labels, training, output = pickle.load(f)
        except:

            words = []
            labels = []
            docs_x = []
            docs_y = []

            for intent in data["intents"]:
                for pattern in intent["questionList"]:
                    pattern = gensim.utils.simple_preprocess(pattern)
                    pattern = ' '.join(pattern)
                    wrds = ViTokenizer.tokenize(pattern)
                    wrds = nltk.word_tokenize(wrds)
                    words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intent["label"])

                if intent["label"] not in labels:
                    labels.append(intent["label"])

            # preprocessing
            words = [w for w in words if w not in stop_words]
            words = sorted(list(set(words)))
            labels = sorted(labels)

            training = []
            output = []
            out_empty = [0 for _ in range(len(labels))]

            for x, doc in enumerate(docs_x):
                bag = []
                wrds = [w for w in doc if w not in stop_words]

                for w in words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)

                output_row = out_empty[:]
                output_row[labels.index(docs_y[x])] = 1

                training.append(bag)
                output.append(output_row)

            training = numpy.array(training)
            output = numpy.array(output)

            with open("data/" + self.modelName + ".pickle", "wb") as f:
                pickle.dump((words, labels, training, output), f)
        self.training, self.words, self.output, self.labels = training, words, output, labels

    # train model
    def trainingModel(self):
        training = self.training
        output = self.output

        tensorflow.compat.v1.reset_default_graph()
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)
        model = tflearn.DNN(net)
        model.fit(training, output, n_epoch=890, batch_size=8, show_metric=True)
        model.save("data/" + self.modelName + ".tflearn")

    def loadModel(self):
        training = self.training
        output = self.output

        tensorflow.compat.v1.reset_default_graph()
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)
        model = tflearn.DNN(net)
        model.load("data/" + self.modelName + ".tflearn")
        return model

    def trainAll(self):
        self.trainingModel()
