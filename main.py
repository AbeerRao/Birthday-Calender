birthdays_friends = {}
options = ["1) Show birthdays", "2) Add a birthday"]

while True:
  print(options[0])
  print(options[1])
  print()

  choice = int(input("Enter the number next to the option: "))

  if choice == 1:
    if birthdays_friends != {}:
      name = str(input("What is the name of the person? "))
      print()
      if name in birthdays_friends:
        print(birthdays_friends[name])
        print()
      elif name not in birthdays_friends:
        print("That name is not in the database")
        print()
    elif birthdays_friends == {}:
      print("No value to show please add one")
      print()
  elif choice == 2:
    name_to_add = str(input("What is the name of the person? "))
    if name_to_add in birthdays_friends:
      print("Try again. That person is already in the database")
      print()
    else:
      date_to_add = input("When is their birthday? ")
      print()
      birthdays_friends[name_to_add] = str(date_to_add)
      print(name_to_add + "'s birth date of " + str(date_to_add) + " has been added to the database")
