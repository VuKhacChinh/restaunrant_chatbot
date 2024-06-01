from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from const.Constant import *


class NerService:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("NlpHUST/ner-vietnamese-electra-base")
        self.model = AutoModelForTokenClassification.from_pretrained("NlpHUST/ner-vietnamese-electra-base")
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def getLabels(self, sentence):
        sentence.strip()
        results = self.nlp(sentence)
        addresses = []
        restaurantNames = []

        address = ""
        restaurantName = ""
        flag = "none"
        for result in results:
            entity = result['entity']
            word = result['word']

            if entity == firstAddressLabel:
                if flag == "address":
                    addresses.append(address)
                else:
                    if flag == "restaurantName":
                        restaurantNames.append(restaurantName)

                flag = "address"
                address = word
            else:
                if entity == middleAddressLabel:
                    address = address + " " + word
                else:
                    if entity[0] == "B":
                        if flag == "address":
                            addresses.append(address)
                        else:
                            if flag == "restaurantName":
                                restaurantNames.append(restaurantName)

                        flag = "restaurantName"
                        restaurantName = word
                    else:
                        restaurantName = restaurantName + " " + word

        if flag == "address":
            addresses.append(address)
        else:
            if flag == "restaurantName":
                restaurantNames.append(restaurantName)

        return addresses, restaurantNames
