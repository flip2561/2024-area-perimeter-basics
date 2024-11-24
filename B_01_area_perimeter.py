# Ask user for width and loop until they
# enter a number that is more then zero
def num_check(question):
    error = "Please entar a number that is more then zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

keep_going =""
while keep_going == "":
    width = num_check("width: ")
    height = num_check("height:  ")
    cost_m = num_check("cost/m?")
    area = width * height
    perimeter = 2 * (width + height)
    cost =perimeter * cost_m
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units ")
    print(f"cost:{cost}$ ")
    keep_going = input("press enter to keep going or any key to quit")
    print()

print("Thank you for using the area / perimeter calculator")