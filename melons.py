# import csv so files can be read or written using DictReader and DictWriter
import csv

# Declare the class name
class Melon():

    # instantiate the class, define it's keys
    def __init__ (self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless
    
    # Defines what is printed when Melon obj is read
    def __repr__(self):
        return (
            f"<melon: {self.melon_id}, {self.common_name}>"
        )
    
    # Prints price in proper format
    def price_str(self):
        return(
            f"${self.price:.2f}"
        )

# empty dictionary to be populated using DictReader
melon_dict = {}

# opens melons.csv and reads line by line
with open ("melons.csv") as csvfile:
    csv_reader = csv.DictReader(csvfile)

    # for each line read, do this
    for row in csv_reader:

        # set variable melon_id equal to this row's melon_id
        melon_id = row['melon_id']

        # set variable melon equal to a new Melon object
        melon = Melon(

            # pass in melon_id of the row being read as the melon_id of this object
            melon_id,
            row['common_name'],

            # csv can't do type conversion, so we do it manually here
            float(row['price']),
            row['image_url'],
            row['color'],

            # use eval so that non-empty strings will not always evaluate to true
            eval(row['seedless'])
        )

        # adds key value pair melon_id to melon_dict, then sets the value to be the new Melon obj
        # this helps make melon_dict searchable instead of simply being a list of objects
        melon_dict[melon_id] = melon

# Returns a list that contains melon_dict's values
def get_all():
    return list(melon_dict.values())

# Returns the object with the specified ID
def get_by_id(melon_id):
    return melon_dict[melon_id]