# import libraries 
import pandas

# *** Functions go here ***

# Checks that input is either a float or an interger that is more than zero
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

# Checks that user has entered yes/no to a question 
      
def yes_no (question):

  to_check = ["yes", "no"]

  valid = False 
  while not valid: 

    # ask question and put response in lowercase 
    response = input(question).lower()

    for var_item in to_check: 
      if response == var_item:
        return response 
      elif response == var_item [0]:
        return var_item 

    print ("Please enter either yes or no... \n")


def not_blank (question, error):
    
    valid = False
    while not valid:
      response = input (question)

      # If the name is not blank, program continues 
      if response == "":
          print ("{}. \n Please try agian.\n".format(error))
          continue 
  
      return response 




def currency(x):
  return "${:.2f}".format(x)
\

def get_expenses(var_fixed):

  # set up dictionaries and lists 
  item_list = []
  quantity_list = []
  price_list = []
  
  variable_dict = {
    "Item": item_list, 
    "Quantity": quantity_list, 
    "Price": price_list
  }
  
  # Loop to get component, quantity and price
  item_name = ""
  while item_name.lower() != "xxx":
  
    print ()
    # Get name, quantity and item
    item_name = not_blank (" Item name: ", "The compopnent name can't be blanket.")
    if item_name.lower() == "xxx":
      break

    if var_fixed == "variable": 
      quantity = num_checker("Quantity: ", "The amount must be a whole number more than zero", )

    else:
      quantity = 1 
      
    price = num_checker("How much for a single item? $", "The price must be a number <more than 0>", )
  
    # Add item, quantity and price to lists 
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)
  
  expenses_frame = pandas.DataFrame (variable_dict)
  expenses_frame = expenses_frame.set_index('Item')
  
  # Calculate cost of each component 
  expenses_frame['Cost'] = expenses_frame['Quantity'] * expenses_frame ['Price']
  
  # Find sub total
  sub_total = expenses_frame ['Cost'].sum ()
  
  # Currency formatting (uses currency function)
  add_dollars = ['Price', 'Cost']
  for item in add_dollars: 
    expenses_frame[item] = expenses_frame[item].apply(currency)

  return [expenses_frame, sub_total ]
\

# **** MAIN ROUTINE GOES HERE ****
# Get product name
product_name = not_blank("Product name: ", "The product name cant't be blank")

print("Let's get the variable costs...")
# Get variable costs 
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable = variable_expenses[1]

print()

have_fixed = yes_no("Do you have fixed costs (y / n)? ")

if have_fixed == "yes":

  # Get fixed costs 
  fixed_expenses = get_expenses("fixed")
  fixed_frame = fixed_expenses[0]
  fixed_sub = fixed_expenses[1]

else:
  fixed_frame = ""
  fixed_sub = 0

# Find total costs 

# Ask user for profit goal 

# Calculate recommended price

# Write data to file

# *** Printing area *** 
print("**** Variable Costs ****")
print(variable_frame)
print()

print ("Variable Costs: ${:.2f}".format (variable_sub))

print()

if have_fixed == "yes":

  print("**** Fixed Costs ****")
  print(fixed_frame)
  print()
  
  print ("Fixed Costs: ${:.2f}".format (fixed_sub))



