from service.TrainingService import TrainingService
from utils.Algorithms import getBagOfWords
from const.Constant import *


class PredictService:
    def __init__(self, modelName):
        self.trainingService = TrainingService(modelName)
        self.model = self.trainingService.loadModel()

    def getLabels(self, question):
        results = self.model.predict([getBagOfWords(question, self.trainingService.words)])
        results = results[0]
        labelResults = []
        for i in range(0, len(results)):
            if results[i] > thresh:
                labelResults.append(self.trainingService.labels[i])
        return labelResults
