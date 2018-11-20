# maths
print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("What is 3 + 2?", 3 + 2)
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# variables
cars = 100
space_in_a_car = 4.0
cars_color = "White"
text = "There are %d %s cars available with %d spaces in each car with a total of %d spaces" % (cars, cars_color, space_in_a_car, cars * space_in_a_car)
print("There are", cars, cars_color, "cars available with ", space_in_a_car, " spaces in each car with a total of ", cars * space_in_a_car, " spaces")
print("There are %d %s cars available with %d spaces in each car with a total of %d spaces" % (cars, cars_color, space_in_a_car, cars * space_in_a_car))
print ("Check: %r" % text)
