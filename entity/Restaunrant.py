class Restaurant:
    def __init__(self, name, address, menu):
        self.name = name
        self.address = address
        self.menu = menu

    def formatMenu(self):
        menuInfo = "Đây là thực đơn của nhà hàng " + self.name + ":\n"
        for food in self.menu:
            menuInfo += food + "\n"
        return menuInfo

    def toString(self):
        return "Nhà hàng " + self.name + " có địa chỉ tại " + self.address


restaurantList = [
    Restaurant("Hà Nội Phố", "Hà Nội", ["bún đậu", "bún cá"]),
    Restaurant("Tây Hồ Quán", "Tây Hồ", ["gà quay", "chè bưởi"]),
    Restaurant("Sơn Lâm", "Phú Thọ", ["Lẩu thái", "bánh tráng trộn"]),
    Restaurant("Thái Nguyên hàng", "Thái Nguyên", ["bún trộn", "bánh mì nướng"]),
    Restaurant("Cơm Đảo", "Bắc Ninh", ["gà rán", "gà chiên"]),
    Restaurant("Quán Gió", "Bắc Giang", ["gà quay", "cá nướng"]),
    Restaurant("Chè ngon quán", "Sài Gòn", ["nem nướng", "bún cá"])
]