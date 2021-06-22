import csv

class CoffeeJournal:
    def __init__(self, file):
        self._file = file
        self._roaster = ""
        self._country = ""
        self._region = ""
        self._stars = ""
        self._new_coffee = [] # Has been read from journal
        self._old_coffee = self.load_coffee()
    @property
    def roaster(self):
        return self._roaster
    @roaster.setter
    def roaster(self, new_roaster):
        self._roaster = new_roaster
    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, new_country):
        self._country = new_country
    @property
    def region(self):
        return self._region
    @region.setter
    def region(self, new_region):
        self._region = new_region
    @property
    def stars(self):
        return self._stars
    @stars.setter
    def stars(self, new_stars):
        self._stars = new_stars

    def load_coffee(self):
        coffee = []
        with open(self._file) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                coffee.append(row)
        return coffee

    def add_coffee(self):
        self._new_coffee.append([self._roaster, self._country, self._region, self._stars])

    def save(self):
        with open(self._file, 'a') as f: #in append mode
            writer = csv.writer(f)
            writer.writerows(self._new_coffee)
    
    def show_coffee(self):
        print()
        # if there is no information on any coffee, tell the user to add one
        if len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
            print("Enter a coffee first")
        # if there is information in the CSV but not new coffee print the old coffee
        elif len(self._old_coffee) > 2 and len(self._new_coffee) == 0:
            for row in self._old_coffee:
                print(f"{row[0]:13} {row[1]:13} {row[2]:13}  {row[3]:13}")
        # print both the old coffee and the new coffee
        else:
            for row in self._old_coffee:
                print(f"{row[0]:13} {row[1]:13} {row[2]:13}  {row[3]:13}")
            for row in self._new_coffee:
                print(f"{row[0]:13} {row[1]:13} {row[2]:13}  {row[3]:13}")
        print()


# **********************************************
# code for testing your script
# **********************************************

test_object2 = CoffeeJournal("test_journal1.csv")
test_object2.show_coffee()


# test_object = CoffeeJournal("test_journal1.csv")
# print(test_object._old_coffee)
# test_object = CoffeeJournal("test_journal1.csv")
# test_object.roaster = "Peace River"
# test_object.country = "Rawanda"
# test_object.region = "Remera"
# test_object.stars = "***"
# print(test_object.roaster)
# print(test_object.country)
# print(test_object.region)
# print(test_object.stars)