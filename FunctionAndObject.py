# LEARNING HOW TO RUN FUNCTIONS AND OBJECTS.
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)
generate_trip_instructions("Central Park")
#THE IDEA BEHIND THIS IS HOW TO RUN A PERAMITOR THIS ISN'T THAT FAR OFF OF THE WAY LISTS WORK.

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  overall_price = hotel_total + car_rental_total + plane_ticket_price
  print(car_rental_total)
  print(hotel_total)
  print(overall_price)

  print("Congrats! Your rental car total is " + str(car_rental_total) + ". Your hotel stay costs " + str(
    hotel_total) + ". Your plane ticket costs " + str(
    plane_ticket_price) + " The total cost of your vacation comes out to " + str(
    hotel_total + car_rental_total + plane_ticket_price) + ". Enjoy your trip!")


calculate_expenses(200, 100, 100, 5)

first_destination=""
second_destination=""
final_destination=""
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark","France","Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn","Queens")
#first name sure and define veriables above the function to get it to print, will have to check on that one.
#second if not sure about the order and want to double check your work, make sure and define in the peramitors what you want to happen.