import datetime
import csv
def get_number(prompt):
  """keep asking till user type valid number"""
  while True :
    try :
      number = int(input(prompt))
      if number < 0:
       print("Number cannot be Negative! try again")
       continue
      return number
    except:
      print("Invalid! please enter numbers only")
def get_text(prompt):
  while True:
    try:
      text = input(prompt).lower().strip()
      if text =="":
        print("cannot be empty! try again")
      else:
        return text
    except: 
      print("invalid! please enter text only")
def load_data():
  cars = {}
  try:
    file = open("Benz.garage.csv", "r")
    for line in file:
      model, year, color, price, qty= line.strip().split(",")
      cars[model] = {"year": int(year), "color": color, "price": int(price), "quantity": int(qty)}
    file.close()
    print("loaded", len(cars), "cars from file")
  except:
    print("no saved file found, starting from fresh!")
  return cars 
def save_data(cars):
  file = open("Benz.garage.csv", "w")
  for model, data in cars.items():
    file.write(model + "," + str(data["year"]) + "," + data["color"] + "," + str(data["price"]) + "," + str(data["quantity"]) + "\n")
  file.close()
def garage_report(cars):
  if len(cars) ==0:
    print("no cars yet")
    return
  total_value = 0
  total_cars = 0
  most_expensive = 0
  for model, data in cars.items():
    car_value = data["price"]* data["quantity"]
    total_value += car_value
    total_cars += data["quantity"]
    if data ["price"] > most_expensive:
      most_expensive = data["price"]
      model_expensive = model
  print("\n--- BENZ GARAGE REPORT---")
  print("total cars models:", len(cars))
  print("total cars in stock:", total_cars)
  print("total inventory value: $", total_value)
  print("most expensive car:", model_expensive, " - $", most_expensive)
def show_all_cars(cars):
  print("\n---- ALL CARS----")
  print("Model". ljust(15), "year". ljust(6), "color". ljust(10), "price". ljust(10), "Qty")
  print("-"*60)
  for model, data in cars.items():
    print(model.ljust(15),str(data["year"]).ljust(6), data["color"].ljust(10), ("$" + str(data["price"])).ljust(10), data["quantity"])
cars = load_data()
def search_by_color(cars):
  target_color = get_text("enter color to search: ").lower().strip()
  found = False
  print("\n---CARS WITH COLOR---", target_color.upper(), "---")
  for model, data in cars.items():
    if data["color"].lower().strip() == target_color:
      print(model.ljust(15), str(data["year"]).ljust(15), data["color"].ljust(10), ("$" + str(data["price"])).ljust(10), data["quantity"])
      found = True
  if found == False:
    print("No cars found with color:", target_color)
def export_to_csv(cars):
  filename = "Benz_garage_report.csv"
  with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["model", "year", "color", "price", "quantity"])
    for model, data in cars.items():
      writer.writerow([model, data["year"], data["color"], data["price"], data["quantity"]])
  print("Report expected to", filename, "✅open it with excel")
while True:
  print("1. Add Car")
  print("2. Show All Cars")
  print("3. Delete Car")
  print("4. Update Car")
  print("5. Search by Car")
  print("6. Search By Color")
  print("7. Garage Report")
  print("8. Export For Excel (Csv)")
  print("9.  Save & Exit")
  choice = input("Enter choice 1-9: ")
  if choice == "1":
    model = get_text("Enter car model:")
    year = get_number("Enter  year:")
    color = get_text("Enter color:")
    price = get_number("Enter price")
    qty = get_number("Enter quantity")
    cars[model] = {"year": year, "color": color, "price": price, "quantity": qty}
    save_data(cars)
    print(model, "Added")
  elif choice == "2":
    show_all_cars(cars)
    if len(cars) == 0:
      print("No cars in garage")
  elif choice == "3":
    delete_car = input("which car do you want to delete? ").lower().strip()
    if delete_car in cars:
      del cars[delete_car]
      save_data(cars)
      print(delete_car, "has been removed from Benz garage! ")
    else:
      print("sorry,", delete_car, "is not in the Benz garage! ")
  elif choice == "4":
    update_car = get_text("which car do you want to update? ").lower().strip()
    if update_car in cars:
      print("1. model 2. year 3. color 4. price 5. quantity 6. All")
      sub_choice = input("1, 2, 3, 4, 5 or 6:")
      if sub_choice == "1":
        try:
          new_model = get_text("enter new model:")
          cars[new_model]= cars.pop(update_car)
          save_data(cars)
          print("model updated")
        except:
          print("Invalid! model must be text")
      elif sub_choice == "2":
        try:
          cars[update_car]["year"]= get_number("enter new year:")
          save_data(cars)
          print("year updated")
        except:
          print("Invalid! year must be numbers")
      elif sub_choice == "3":
        try:
          cars[update_car]["color"]= get_text("enter new color:")
          save_data(cars)
          print("color updated")
        except:
          print("Invalid! color must be text")
      elif sub_choice == "4":
        try:
          cars[update_car]["price"]= get_number("enter new price:")
          save_data(cars)
          print("price updated")
        except:
          print("Invalid! price must be number")
      elif sub_choice == "5":
        try:
         cars[update_car]["quantity"]= get_number("enter new quantity:")
         save_data(cars)
         print("quantity updated")
        except:
          print("invalid! quantity must be number")
      elif sub_choice == "6":
        try:
          new_model = get_text("enter new model: ")
          cars[new_model]= cars.pop(update_car)
          cars[new_model]["year"]= get_number("enter new year:")
          cars[new_model]["color"]= get_text("enter new color:")
          cars[new_model]["price"]= get_number("enter new price:")
          cars[new_model]["quantity"]= get_number("enter new quantity:")
          save_data(cars)
          print("All details updated!")
        except:
          print("invalid! year, price and quantity must be numbers.")
    else:
        print("sorry,", update_car, "is not in the Benz garage!")
  elif choice == "5":
    search = get_text("search car model: ")
    if search in cars:
      data = cars[search]
      print("---FOUND---")
      print("model:", search, "year:", data["year"], "color:", data["color"], "price: $", data["price"], "Qty:", data ["quantity"])
    else:
      print("sorry,", search, "is not in Benz garage yet!")
  elif choice == "6":
    search_by_color(cars)
  elif choice == "7":
    garage_report (cars)
  elif choice == "8":
    export_to_csv (cars)
  elif choice == "9":
    save_data(cars)
    print("data saved! thank you for using Benz Barage bye👋")
    break
  else:
    print("invalid choice, enter 1-9")
       
     