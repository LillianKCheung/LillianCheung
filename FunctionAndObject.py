# LEARNING HOW TO RUN FUNCTIONS AND OBJECTS.

# this first code is working as a divider for other projects in this file. This make it easier to tell them apart.
def print_devider():
  print("/----------------------------------------------------------------------------------------/")


def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)
generate_trip_instructions("Central Park")
#String will output in place of location parameter.

print_devider()

#This code is here demonstrating conatonation.
# Please note that fed in parameters are int and therefore str needs to be added to keep code from breaking.
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

print_devider()

# continued practice with fuctions and parameters.
first_destination=""
second_destination=""
final_destination=""
def trip_planner(first_destination, second_destination, final_destination="San Juan Islands"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark","France","Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn","Queens")
# There are a few concepts here. We have set up empty strings outside of the function. The third parameter is set in the function which
#allows this to be a default option.
#line 35 demonstrates that it is possible to call a parameter name explicitly and the code will output in the order placed within the function.

print_devider()

#USING BUILT IN FUNCTIONS: VERIABLES ARE ADDED LIKE PERAMETERS AND THEN SEARCHED FOR INFO FROM THE PERAMETERS
#The variables are added in much the same way a empty string would be used.
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 115.99
poster_price = 2.00
# The builtin function demonstrated here is max. The output will give the highest total int on a given variable.
max_price=max(tshirt_price, shorts_price,mug_price,poster_price)
print(max_price)

print_devider()
#The following code is application of the project directly above.
#THE POINT OF THIS IS THAT YOU CAN KEEP A BUDGET ON HERE BY PASSING PARAMETERS IN AND KEEPING A RUNNING TALLY.
# As a matter of organization there are two functions for this one that will show the current amount in the budget.
#The second function will show how parameters can interact and how to return code.
# One function is keeping track of the print statements and the second function is taking care of the mathmatical operations.
current_budget = 3500.75
shirt_expense=9.00
def print_remaining_budget(budget):
  print("Your current budget is: $" + str(budget))

print_remaining_budget(current_budget)
def deduct_expense(budget, expense):
  return budget-expense


new_budget_after_shirt=deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

print_devider()
#This next function is demonstrating the built in function Max Num. This is also starting to demonstrate if else statements.

def max_num (num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num1 == num2 or num1 == num3:
    return "It's a tie!"
  elif num2 > num1 and num2 > num3:
    return num2
  elif num2 == num1 or num2 == num3:
    return "It's a tie!"
  elif num3 > num2 and num3 > num1:
    return num3
  elif num3 == num2 or num3 == num1:
    return "It's a tie!"

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

print_devider()

# this code is demonstrating having a list as a parameter. It is also demonstrating using the builtin function len.
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list

print(append_size([23, 42, 108]))

print_devider()

#This is the use of the builtin function range. In the return for the function we have a start that is initiated by the parameter.
#The next two places in the return are the number it will stop at NON INCLUSIVE and the increment it will follow.
def every_three_nums(start):
  return list(range(start,101,3))
print(every_three_nums(25))

print_devider()


#this code is demonstrating the use of mod as well as boolean logic. This is also a beginning demonstration of for loops.
def divisible_by_ten(nums):
  count=0
  for num in nums:
    if num%10==0:
      count+=1
  return count
print(divisible_by_ten([20, 25, 30, 35, 40]))

print_devider()

#the creation of a new list with a for loop.
def add_greetings(names):
  greeting=[]
  for name in names:
    greeting.append("Hello, " + name + "!" +" How would you like to be greeted today?")
  return greeting
print(add_greetings(["violet","Tyberius","Augustus"]))

print_devider()

#style of making code work changed at thsi point which is why there is a list that is commented out at the top of this next function.
# the idea is to start the code at the basics and make it run and after the code is running then add it into a function and worry about returning its values.
# my_list=[4,48,88,22,111,12,13]
#note that the second demonstrated list is empty. This means that the code has the ability to pop items off the list and stop at the end of the list.
def delete_starting_evens(my_list):
  while len(my_list)>0:
    if my_list[0]%2==0:
      my_list.pop(0)
    else:
      break
  return my_list
# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
print_devider()


#This is a different version of using a range. This time using len with a range and an i as a counter.
# In running this code I need to be careful of how i and len are used so that the code doesn't break out of range.
def odd_indices(my_list):
  new_list=[]
  for i in range(len(my_list)):
    if i % 2 ==0:
      continue
    else:
      new_list.append(my_list[i])
  return new_list
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

print_devider()

#this code is demonstrating nested loops. Note that I is established inside of the for loop.
# The reason base[i] and powers [j] are needed is to append new numbers into a list.
#also note that when the code is done correctly the list lengths do not have to match.
def exponents(bases, powers):
  exp = []
  for i in range(len(bases)):
    for j in range(len(powers)):
      exp.append(bases[i] ** powers[j])
  return exp
print(exponents([2, 3], [1, 2, 3,5,6]))
print_devider()
# this is just more practice.
num=[]
for i in range(10):
  i += 1
  num.append(i)
print(num)
print_devider()

#this is a demonstration of for loops with if else statements within the same function.
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for i in range(len(lst1)):
    sum1 += lst1[i]
  for j in range(len(lst2)):
    sum2 += lst2[j]
  if sum1 > sum2:
    return lst1
  else:
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7,10]))

print_devider()
