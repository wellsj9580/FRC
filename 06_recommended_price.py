import math 


def num_checker (question, num_type):
  vaild = False 
  while not vaild:

    error = "Please enter a number that is more than zero"

  # ask user for number and check it is valid 
    try: 

      if num_type == "int":
        response = int(input (question))
        error = "Please enter a whole number over 0"
      else :
        response = float(input(question))
        error = "Please enter a number over 0"
  
      if response > 0:
         return response
      else:
         print(error)
      
        # if an interger is not entered, display and error 
    except ValueError: 
      print (error)
\

def round_up(amount, var_round_to):
  return int(math.ceil(amount / round_to)) * round_to

# Main routine starts here 
how_many = num_checker("How many items?", int)
total = num_checker("Total Costs? ", float)
profit_goal = num_checker("Profit Goal? ", float)
round_to = num_checker("Round to nearest...? ", int)

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print("Profit Goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed / how_many 
print ("Selling Price (unrounded) : ${:.2f}".format(selling_price))

recommended_price = round_up (selling_price, round_to)
print("Recommended Price: ${:.2f}".format(recommended_price))
