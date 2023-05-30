list_cars = ['BMW', 'Man', 'volwagen', 'BENZ' ,'Honda']

list_cars.append('Volvo')
list_cars.remove('Honda')

print(list_cars)

# Output: ['BMW', 'MAN', 'VOlWAGEN', 'BENZ' , 'HONDA']

##
list_cars = ['BMW', 'Man', 'volwagen', 'BENZ' ,'Honda']
current_list_cars = "-"
list_cars = [] # create an empty list

while current_list_cars!= '0':
    if current_list_cars in "1234":
        print("Adding {}".format(current_list_cars))
        if current_list_cars == '1':
            list_cars.append("BMW")
        elif current_list_cars== '2':
            list_cars.append("MAN")
        elif current_list_cars == '3':
            list_cars.append("VOLWAGEN")
        elif current_list_cars == '4':
            list_cars.append("BENZ")
        elif current_list_cars == '5':
            current_list_cars.append("HONDA")
    else:
        print("Please add options from the list below:")
        print("1: ")
        print("2: BMW")
        print("3: MAN")
        print("4: VOLWAGEN")
        print("5: BENZ")
        print("0: to finish")

    current_list_cars = input()
##
# Task 2
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"
                   ]
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse mat")
        elif current_choice == '6':
            computer_parts.append("hdmi cable")
    else:
        print("Please add options from the list below:")
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part) + 1, part))

    current_choice = input()

print(computer_parts)

#task 2

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]
#valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)
# Task1
fruits = {"Apples","Cherries", "Strawberries" }
for fruits in fruits:
    print(fruits)