def get_number(promt):
  """ keep asking until the user type a valid number. No crashes """
  while True:
    try:
      number = int(input(promt))
      if number < 0:
        print("Number cannot be negative! try again")
        continue
      return number
    except:
      print("Invalid! please enter numbers only")
def get_text(promt):
  while True:
    text = input(promt).lower().strip()
    if text == "":
      print("cannot be empty! try again")
    else:
      return text
import datetime
def export_to_csv(students):
  """ export all students data to csv file that can be opened in Excel"""
  file = open("report.csv", "w")
  file.write("Name, Age, City, Laptop_money \n")
  for name, data in students.items():
    file.write(name + "," + str(data["age"]) + "," + data["city"] + "," + str(data["laptop_money"]) + "\n")
  file.close()
  print("Report exported to report.csv✅ open it with Excel!")
def backup_data(students):
  """ create a backup file with today's date so data is never lost"""
  today = datetime.datetime.now().strftime("%y-%m-%d") # Gets today's date like 23-08-2026
  backup_filename = "Benz_garage_backup_" + today + ".txt"
  file = open(backup_filename, "w")
  for name, data in students.items():
    file.write(name + "," + str(data["age"]) + "," + data["city"] + "," + str(data["laptop_money"]) + "\n")
  file.close()
  print("backup saved as:", backup_filename, "✅")
def load_different_file():
  filename = input("Enter filename to load: ")
  students = {}
  try:
    file = open(filename, "r")
    for line in file:
      name, age, city, money = line.strip().split(",")
      students[name]= {"age": int(age), "city": city, "laptop_money": int(money)}
    file.close()
    print("loaded", len(students), "students from", filename, "✅")
  except:
    print("File not found! check spelling")
  return students
def load_data():
  students = {}
  try:
    file = open("Benz_garage.txt", "r")
    for line in file:
      name, age, city, money = line.strip().split(",")
      students[name]= {"age": int(age), "city": city, "laptop_money": int(money)}
    file.close()
    print("loaded", len(students), "students from file✅")
  except:
    print("no saved file found. starting fresh!")
  return students
def save_data(students):
  file = open("Benz_garage.txt", "w")
  for name, data in students.items():
    file.write(name + "," + str(data["age"]) + "," + data["city"] + "," + str(data["laptop_money"]) + "\n")
  file.close()
def show_all_students(students):
  print("\n--- ALL STUDENT---")
  print("Name".ljust(10), "Age".ljust(5), "City".ljust(10), "Money")
  print("-"*40)
  for name, data in students.items():
    print(name.ljust(10),str(data["age"]).ljust(5), data["city"].ljust(10),data["laptop_money"])
students = load_data()
def search_by_city(students):
  target_city = input("Enter city to search: ").lower().strip()
  found = False
  print("\n---STUDENTS IN", target_city.upper(), "---")
  for name, data in students.items():
    if data["city"]== target_city:
      print(name.ljust(10), str(data["age"]).ljust(5), data["city"].ljust(10), data["laptop_money"])
      found = True
  if found ==False:
    print("No student found in", target_city)
def sort_by_money(students):
  print("\n---STUDENTS SORTED BY MONEY RICHEST FIRST---")
  # sort students by money. x[1] is the data. Reverse=True  = biggest first
  sorted_students = sorted(students.items(), key=lambda x: x[1]["laptop_money"], reverse= True)
  print("NAME".ljust(10), "AGE".ljust(5), "CITY".ljust(10), "MONEY")
  print("-"*40)
  for name, data in sorted_students:
    print(name.ljust(10), str(data["age"]).ljust(5), data["city"].ljust(10), data["laptop_money"])
while True:
  print("\n==== Benz Garage System====")
  print("1. Report")
  print("2. search student")
  print("3. Add student")
  print("4. Delete student")
  print("5. Update student")
  print("6. Show_all_students")
  print("7. Search by City")
  print("8. Sort by Money")
  print("9. Save & Exit")
  print("10. Backup Data")
  print("11. Load Different Data")
  print("12. Export to Excel/Csv")
  print("13. Garage Statistics")
  choice = input("Enter 1-13: ")
  if choice == "1":
    if len(students) == 0:
      print("no students yet!")
    else:
      richest_name = ""
      richest_money = 0
      poorest_name = ""
      poorest_money = float('inf')
      total_money = 0
      count = 0
      for name, data in students.items():
        if data["laptop_money"] > richest_money:
          richest_money = data["laptop_money"]
          richest_name = name
        if data["laptop_money"] < poorest_money:
          poorest_money = data["laptop_money"]
          poorest_name = name
        total_money = total_money + data["laptop_money"]
        count = count + 1
      average = total_money / count
      print("---Benz Garage Report---")
      print("RICHEST:", richest_name, richest_money, "naira")
      print("POOREST:", poorest_name, poorest_money, "naira")
      print("AVERAGE:", round(average, 2), "naira")
  elif choice == "2":
    search_name = input("who do you want to search? ").lower().strip()
    if search_name in students:
      person = students[search_name]
      print("---FOUND---")
      print("Name:", search_name, "Age:", person["age"], "City:", person["city"], "Money:", person["laptop_money"])
    else:
      print("sorry,", search_name, "is not in Benz garage yet!")
  elif choice == "3":
    new_name = get_text("Enter new name: ").lower().strip()
    if new_name in students:
      print(new_name, "is already in Benz garage!")
    else:
      new_age = get_number("Enter new age: ")
      new_city = get_text("Enter new city: ").lower().strip()
      money = get_number("Enter new money: ")
      students[new_name] = {"age": new_age, "city": new_city, "laptop_money": money}
      save_data(students)
      print(new_name, "has been added to Benz garage! ")
  elif choice == "4":
    delete_student = input("who do you want to delete? ").lower().strip()
    if delete_student in students:
      del students[delete_student]
      print(delete_student, "has been removed from Benz garage! ")
    else:
      print("sorry,", delete_student, "is not in the Benz garage! ")
  elif choice == "5":
    update_name = get_text("who do you want to update? ").lower().strip()
    if update_name in students:
      print("1. Age 2. City 3. Money 4. All")
      sub_choice = input("1, 2, 3, or 4:")
      if sub_choice == "1":
        try:
         students[update_name]["age"]= get_number("Enter new age: ")
         save_data(students)
         print("age updated!")
        except:
          print("invalid! Age must be numbers")
      elif sub_choice == "2":
        students[update_name]["city"]= get_text("Enter new city: ").lower().strip()
        print("city updated!")
      elif sub_choice == "3":
        try:
         students[update_name]["laptop_money"]= get_number("Enter new laptop_money: ")
         print("laptop_money updated!")
        except:
          print("invalid! Money must be numbers")
      elif sub_choice == "4":
        try:
         students[update_name]["age"]= get_number("Enter new age: ")
         students[update_name]["city"]= get_text("Enter new city: ").lower().strip()
         students[update_name]["laptop_money"]= get_number("Enter new laptop_money: ")
         save_data(students)
         print("All details updated!")
        except:
          print("invalid! Age and Money must be numbers")
      else:
        print("invalid choice")
    else:
      print("sorry,", update_name, "is not in the Benz garage!")
  elif choice == "6":
    show_all_students(students)
  elif choice == "7":
    search_by_city(students)
  elif choice == "8":
    sort_by_money(students)
  elif choice == "10":
    backup_data(students)
  elif choice == "11":
    students = load_different_file()
  elif choice == "12":
    export_to_csv(students)
  elif choice == "13":
    if len(students) == 0:
      print("No students yet!")
    else:
      total_students = len(students)
      total_money = 0
      total_age = 0
      for name, data in students.items():
        total_money = total_money + data["laptop_money"]
        total_age = total_age + data["age"]
      Average_age = total_age / total_students
      print("\n---GARAGE STATISTICS---")
      print("Total Students:", total_students)
      print("Total Money In Garage:", total_money, "naira")
      print("Average Age:", round(Average_age, 1))
      print("----------\n")
  elif choice == "9":
    save_data(students)
    print("data saved! thank you for using Benz Garage! bye👋")
    break
  else:
    print("invalid choice, Enter 1-13")