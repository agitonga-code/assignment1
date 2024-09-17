class MenuItem:
    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        return self._name

    def get_wholesale_cost(self):
        return self._wholesale_cost

    def get_selling_price(self):
        return self._selling_price


class SalesForDay:
    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        return self._day

    def get_sales_dict(self):
        return self._sales_dict


class SmochaStand:
    def __init__(self, name,location):
        self._name = name
        self._location = location
        self._current_day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        return self._name

    def add_menu_item(self, menu_item):
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        for item, quantity in sales_dict.items():
            if item not in self._menu:
                raise InvalidSalesItemError(f"Item '{item}' not found in menu")
        self._sales_record.append(SalesForDay(self._current_day, sales_dict))
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, item_name):
        for sale in self._sales_record:
            if sale.get_day() == day:
                sales_dict = sale.get_sales_dict()
                return sales_dict.get(item_name, 0)
        return 0

    def total_sales_for_menu_item(self, item_name):
        total_sales = 0
        for sale in self._sales_record:
            sales_dict = sale.get_sales_dict()
            total_sales += sales_dict.get(item_name, 0)
        return total_sales

    def total_profit_for_menu_item(self, item_name):
        menu_item = self._menu.get(item_name)
        if not menu_item:
            return 0 
        total_sales = self.total_sales_for_menu_item(item_name)
        profit_per_item = menu_item.get_selling_price() - menu_item.get_wholesale_cost()
        return total_sales * profit_per_item

    def total_profit_for_stand(self):
        total_profit = 0
        for item_name in self._menu:
            total_profit += self.total_profit_for_menu_item(item_name)
        return total_profit

if __name__ == "__main__":
    stand = SmochaStand( 'Spicy Corner',"Langata")
    item1 = MenuItem('Smocha', 50,
                     75)
    stand.add_menu_item(item1)
    item2 = MenuItem('HotDog', 30,
                     50)
    stand.add_menu_item(item2)
    item3 = MenuItem('Chai', 10, 25)
    stand.add_menu_item(item3)
    day_0_sales = {'Smocha': 17, 'HotDog': 25}

    stand.enter_sales_for_today(day_0_sales)  
    print(f"Smocha profit = {stand.total_profit_for_menu_item('Smocha')}")


