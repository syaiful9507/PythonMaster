class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def add_distances(self, distance):
        result_inches = self.inches + distance.inches
        result_feets = self.feet + distance.feet

        # while inch is 12 or greather,
        # increase feet by 1 and decrease inches by 12
        while(result_inches >= 12):
            result_feets = result_feets + 1
            result_inches = result_inches - 12

        # create an object of Dictance
        result_distance = Distance(result_feets, result_inches)
        return  result_distance
# create distance1 object
distance1 = Distance(12,8)

#create distance2 object
distance2 = Distance(10,6)

# call add_distance using distance1 object
# distance2 is user as argument
result = distance1.add_distances(distance2)
print(f'Result distance : {result.feet} ft {result.inches}')