class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        if self.start_time >= 12:
            s_time = str(self.start_time) + 'pm'
        else:
            s_time = str(self.start_time) + 'am'

        if self.end_time >= 12:
            e_time = str(self.end_time) + 'pm'
        else:
            e_time = str(self.end_time) + 'am'
        return f"{self.name} menu will be available from {s_time} to {e_time}"

    def calculate_bill(self, purchased_items):
        total = 0
        for key in purchased_items:
            total += self.items[key]
        return total


# brunch menu object
brunch = Menu("Brunch",
              {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
               'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
               }, 11, 16)

# early bird menu object
early_bird = Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
                                 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)

# dinner menu object
dinner = Menu("Dinner",
              {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
               'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 22)

# kids menu object
kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

print(brunch)
brunch_order_1_total = brunch.calculate_bill(["home fries", "pancakes", "coffee"])
print(f"Your total for the {brunch.name} meal will be: R{brunch_order_1_total}\n")

print(early_bird)
early_bird_order_1_total = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print(f"Your total for the {early_bird.name} meal will be: R{early_bird_order_1_total}")


########################################################################

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"Address: {self.address}"

    def available_menus(self, time):
        quali_menus = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                quali_menus.append(menu.name)
        return quali_menus


menus_list = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus_list)
new_installement = Franchise("12 East Mulberry Street", menus_list)

print()
print(flagship_store)
print(new_installement)

print()
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))


########################################################################

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return f"Welcome to {self.name}\nList of Stores:\n ** - {self.franchises}"


franchises_list = [flagship_store, new_installement]
basta_fazoolin = Business('Basta Fazoolin', franchises_list)

# Creating new business through classes
arepas_menu = Menu("Take a' Arepa",
                   {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
                    }, 10, 20)

# adding new menu to menus list
menus_list.append(arepas_menu)

# print(menus_list)
arepas_place = Franchise("189 Fitzgerald Avenue", menus_list)
arepas_business = Business("Take a' Arepa", arepas_place)

print()
print(basta_fazoolin)
print()
print(arepas_business)
