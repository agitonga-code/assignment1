	# Assignment 1
### You MUST do this assignment alone! If you use existing internet material for your answers, you must provide a citation. AI code generators are strictly prohibited. Any AI generate code will result in a 0 grade for this assignment and you will be reported for misconduct. Always watch the class Piazza channel for updates on assignments. Read all instructions carefully!

# Due: Friday August 16th, 2024

**[140 pts]**  You are the owner of a popular Smocha stand, a favorite street food spot in your neighborhood. Your stand sells a variety of Smocha, each consisting of a delicious samosa placed inside a soft bread roll, often accompanied by tasty sauces. To keep track of your daily sales and manage your menu items, you need to develop a program that will record the items on your menu and track your sales over time. You will be creating code to manage the menu items and track the daily sales of a SmochaStand. This will involve three classes: MenuItem, SalesForDay, and SmochaStand. All data members in each class should be designated as private and they should only be accessed from outside the class using appropriate getter or setter methods. 

Here are the method descriptions for the three classes:


**MenuItem:**

A MenuItem object represents a menu item to be offered for sale at the Smocha stand, which has three data members:
* a string for the item's name
* a float for the item's wholesale cost (how much the stand pays for the item)
* a float for the item's selling price (how much the stand sells the item for)

The Menu Item methods are:
* init method - takes three parameters (name, wholesale cost, selling price) and uses them to initialize the data members
* get methods for each of the data members: get_name(), get_wholesale_cost(), and get_selling_price()


**SalesForDay:**

A SalesForDay object represents the sales for a particular day, which has two data members:
* an integer for the number of days the smocha stand has been open so far
* a dictionary whose keys are the names of the items sold and whose values are the numbers of those items sold that day

The SalesForDay methods are:
* init method - takes two parameters (number of days, sales dictionary) and uses them to initialize the data members
* get methods for each of the data members: get_day() and get_sales_dict()


**SmochaStand:**
**Remember that the SmochaStand class must not directly access the private data members of MenuItem and SalesForDay objects, but instead must call the appropriate get methods**

A SmochaStand object represents five data members: 
* a string for the name of the stand
* a string for the location of the stand
* an integer representing the current day
* a dictionary of MenuItem objects, where the keys are the names of the items and the values are the corresponding MenuItem objects
* a list of SalesForDay objects

The SmochaStand methods are:
* init method - takes one parameter, the name of the stand; initializes the name to that value, the location of the stand; initializes the location to that value, initializes current day to zero, initializes the menu to an empty dictionary, and initializes the sales record to an empty list
* a get method for the name: get_name()
* add_menu_item - takes as a parameter a MenuItem object and adds it to the menu dictionary. New items can be added to the menu on any day
* enter_sales_for_today - takes as a parameter a dictionary where the keys are names of items sold and the corresponding values are how many of the item were sold (see the example at the end of the readme). If an item in the menu doesn't appear in the dictionary, then there were no sales of that item on that day. If the name of any item sold doesn't match the name of any MenuItem in the dictionary of MenuItem objects, this method should do nothing except raise an **InvalidSalesItemError** (you'll need to define this exception class). Otherwise, it should create a new SalesForDay object using the current day and the dictionary that was passed in, add that object to the list of SalesForDay objects, and then increment the current day by 1
* sales_of_menu_item_for_day - takes as a parameter an integer representing a particular day and the name of a menu item. It returns the number of that item sold on that day. This method will use the given day to find the corresponding SalesForDay object in the list and then call its get_sales_dict method to get the dictionary of sales for that day. It will then look for the item name in the dictionary, taking into account that if an item in the menu doesn't appear in the dictionary, then there were no sales of that item on that day
* total_sales_for_menu_item - takes as a parameter the name of a menu item and returns the total number of that item sold over the history of the stand. This method can make use of sales_of_menu_item_for_day
* total_profit_for_menu_item - takes as a parameter the name of a menu item and returns the total profit on that item over the history of the stand. The profit for any item sold is the selling price of the item minus the wholesale cost of the item. This method can make use of total_sales_for_menu_item
* total_profit_for_stand - takes no parameters and returns the total profit on all items sold over the history of the stand. This method can make use of total_profit_for_menu_item

**[30 pts]**  **Your SmotchaStand.py file must include a main function** that runs if the file is run as a script, but not if it's imported to another file.  Your main function should:
1. create a SmochaStand object
2. create one or more MenuItem objects and add them to the SmochaStand's menu
3. create a dictionary of sales for the day that includes sales of at least one item that isn't in the menu
4. try calling enter_sales_for_today(), passing that sales dictionary as the argument
5. If an InvalidSalesItem is raised, it should be caught with a try/except that prints an explanatory message for the user (otherwise the function should proceed normally)

**[30 pts]**  In addition to your file containing the code for the above classes, **you must also submit a file that contains unit tests for your classes.  It must have at least five unit tests and use at least two different assert functions.  This part (like the rest) must be your own work. 

**You do not need to write your own main function or unit tests - I will take care of that.**

Here's a very simple example of how your classes could be used:
```
stand = SmochaStand('Spicy Corner')  # Create a new SmochaStand called 'Spicy Corner'
item1 = MenuItem('Smocha', 0.5, 0.75)  # Create Smocha as a menu item (wholesale cost Kshs: 50 shillings, selling price 75)
stand.add_menu_item(item1)  # Add Smocha to the menu for 'Spicy Corner'
item2 = MenuItem('HotDog'), 0.3, 0.5)  # Create HotDog as a menu item (wholesale cost Kshs: 30, selling price Kshs:50)
stand.add_menu_item(item2)  # Add HotDog to the menu for 'Spicy Corner'
item3 = MenuItem('Chai', 0.1, 0.25  # Create Chai as a menu item (wholesale cost Kshs: 10, selling price Kshs: 25)
stand.add_menu_item(item3)  # Add Chai to the menu for 'Spicy Corner'

# This dictionary records that on day zero, 5 Smocha were sold, 2 HotDogs were sold, and no Chai was sold
day_0_sales = {
    'Smocha' : 17,
    'HotDog'   : 25
}

stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
print(f"Smocha profit = {stand.total_profit_for_menu_item('Smocha')}"  # print the total profit for Smocha so far
```

Your files must be named: **SmochaStand.py** and **SmochaStandTester.py**...And do not forget to edit details given in the student.info file to march your own details.
