from entity.Restaunrant import restaurantList
from service.PredictService import PredictService
from service.NerService import NerService
from const.Constant import *
import json


def getMenuOfRestaurant(restaurants):
    for restaurant in restaurantList:
        if restaurant.name in restaurants:
            return restaurant.formatMenu()

    return ""


def getRestaurantByFood(foods):
    restaurants = []
    for restaurant in restaurantList:
        for food in restaurant.menu:
            if food in foods:
                restaurants.append(restaurant)

    return restaurants


def getRestaurantByAddress(addresses):
    restaurants = []
    for restaurant in restaurantList:
        if restaurant.address in addresses:
            restaurants.append(restaurant)

    return restaurants


def getRestaurantByFoodAndAddress(foods, addresses):
    restaurants = []
    for restaurant in restaurantList:
        if restaurant.address in addresses:
            for food in restaurant.menu:
                if food in foods:
                    restaurants.append(restaurant)

    return restaurants


def getRestaurantByName(name):
    restaurants = []
    for restaurant in restaurantList:
        if restaurant.name in name:
            restaurants.append(restaurant)

    return restaurants


def checkExistByResAndFood(name, food):
    restaurants = []
    for restaurant in restaurantList:
        if restaurant.name == name and food in restaurant.menu:
            return True
    return False


def formatRestaurants(restaurants):
    resInfo = "Đây là danh sách các nhà hàng bạn có thể tham khảo:\n"
    for restaurant in restaurants:
        resInfo += restaurant.toString() + "\n" + restaurant.formatMenu()

    return resInfo


class ChatBotService:
    def __init__(self):
        self.foodService = PredictService("food")
        self.generalService = PredictService("general")
        self.nerService = NerService()
        self.answer = "Bạn muốn ăn gì"

    def chat(self, question):
        generals = self.generalService.getLabels(question)
        addresses, restaurantNames = self.nerService.getLabels(question)
        foods = self.foodService.getLabels(question)

        value = {
            "topics": generals,
            "addresses": addresses,
            "restaurants": restaurantNames,
            "foods": foods
        }

        return json.dumps(value, ensure_ascii=False)

        # if len(generals) > 0:
        #     general = generals[0]
        #     if general == Menu:
        #         if len(addresses) == 0:
        #             self.answer = "Hôm nay có nhiều món ngon như bún cá, bún chả của nhà hàng Tây Long"
        #         else:
        #             self.answer = getMenuOfRestaurant(restaurantNames)
        #
        #         if self.answer == "":
        #             self.answer = "Xin lỗi, nhà hàng bạn tìm không có trên hệ thống"
        #
        #     elif general == Hobby or general == Address:
        #         restaurants = []
        #         if len(foods) == 0:
        #             if len(addresses) > 0:
        #                 restaurants = getRestaurantByAddress(addresses)
        #         else:
        #             if len(addresses) == 0:
        #                 restaurants = getRestaurantByFood(foods)
        #             else:
        #                 restaurants = getRestaurantByFoodAndAddress(foods, addresses)
        #
        #         if len(restaurants) == 0:
        #             self.answer = "Xin lỗi, không có nhà hàng nào đáp ứng nhu cầu của bạn, hãy thử tìm theo thông tin khác"
        #         else:
        #             self.answer = formatRestaurants(restaurants)
        #
        #     elif general == ResAddress:
        #         if len(restaurantNames) == 0:
        #             self.answer = "Xin lỗi, bạn muốn tìm nhà hàng nào?"
        #         else:
        #             restaurants = getRestaurantByName(restaurantNames[0])
        #             self.answer = formatRestaurants(restaurants)
        #
        #     elif general == FoodYN:
        #         if len(foods) == 0 or len(restaurantNames) == 0:
        #             self.answer = "Bạn muốn hỏi điều gì?"
        #         else:
        #             result = checkExistByResAndFood(restaurantNames[0], foods[0])
        #             if result:
        #                 self.answer = "Đúng vậy, nhà hàng " + restaurantNames[0] + "có món " + foods[0]
        #             else:
        #                 self.answer = "Không, nhà hàng " + restaurantNames[0] + "không có món " + foods[0]
        # return self.answer
