class InvalidSalesItemError(Exception):
    pass


class MenuItem:
    def __init__(self, name, wholesale_cost:float, selling_price:float):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def getName(self):
        return self._name

    def getWholesaleCost(self):
        return self._wholesale_cost

    def getSellingPrice(self):
        return self._selling_price


class SalesForDay:
    def __init__(self, number_of_days, sales_dict):
        self._number_of_days = number_of_days
        self._sales_dictionary = sales_dict


    def getNumberOfDays(self):
        return self._number_of_days

    def getSalesDictionary(self):
        return self._sales_dictionary

class SmochaStand:

    def __init__(self, name):
        self._name = name
        self._location = ''
        self._current_day=0
        self._menu={}
        self._sales=[]

    def get_name(self):
        return self._name

    def add_menu_item(self,item ):
        item_name=item.getName()
        if item_name in self._menu :
            print(f"{item_name}is already on the menu")
        else :
            self._menu[item_name]=[item]

    def enter_sales_for_today(self, sales_dict):
        for item in sales_dict.keys():
            if item not in self.__menu:
                raise InvalidSalesItemError(f"Invalid sales item: {item}")

        sales_for_today = SalesForDay(self.__current_day, sales_dict)
        self.__sales_record.append(sales_for_today)
        self.__current_day += 1

    def sales_of_menu_item_for_day(self, day, item_name):
        if day < len(self.__sales_record):
            sales_dict = self.__sales_record[day].get_sales_dict()
            return sales_dict.get(item_name, 0)
        return 0

    def total_sales_for_menu_item(self, item_name):
        total_sales = 0
        for day in self.__sales_record:
            total_sales += day.get_sales_dict().get(item_name, 0)
        return total_sales

    def total_profit_for_menu_item(self, item_name):
        """Calculates total profit for a specific menu item."""
        menu_item = self.__menu.get(item_name)
        if menu_item:
            total_sales = self.total_sales_for_menu_item(item_name)
            profit_per_item = menu_item.get_selling_price() - menu_item.get_wholesale_cost()
            return total_sales * profit_per_item
        return 0

    def total_profit_for_stand(self):
        """Calculates total profit for all items sold."""
        total_profit = 0
        for item_name in self.__menu:
            total_profit += self.total_profit_for_menu_item(item_name)
        return total_profit

    def main():
        stand = SmochaStand('Spicy Corner', 'Main Street')

        item1 = MenuItem('Smocha', 0.5, 0.75)
        stand.add_menu_item(item1)

        item2 = MenuItem('HotDog', 0.3, 0.5)
        stand.add_menu_item(item2)

        item3 = MenuItem('Chai', 0.1, 0.25)
        stand.add_menu_item(item3)

        # This dictionary records sales for day zero
        day_0_sales = {
            'Smocha': 17,
            'HotDog': 25,
            'InvalidItem': 5  # This item is not in the menu
        }

        try:
            stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
        except InvalidSalesItemError as e:
            print(e)

        print(f"Smocha profit = {stand.total_profit_for_menu_item('Smocha')}")
        print(f"Total profit for the stand = {stand.total_profit_for_stand()}")

    if __name__ == "__main__":
        main()




stand = SmochaStand('Spicy Corner')

    # Create MenuItems
item1 = MenuItem('Smocha', 50, 75)  # Smocha item (wholesale cost 50 shillings, selling price 75 shillings)
item2 = MenuItem('HotDog', 30, 50)  # HotDog item (wholesale cost 30 shillings, selling price 50 shillings)
item3 = MenuItem('Chai', 10, 25)  # Chai item (wholesale cost 10 shillings, selling price 25 shillings)

    # Add items to the menu
stand.add_menu_item(item1)
stand.add_menu_item(item2)
stand.add_menu_item(item3)
print (menu)
