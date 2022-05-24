# import libraries 
import pandas
import math

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
\

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


\

def not_blank (question, error):
    
    valid = False
    while not valid:
      response = input (question)

      # If the name is not blank, program continues 
      if response == "":
          print ("{}. \n Please try agian.\n".format(error))
          continue 
  
      return response 




\

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

def expense_print(heading, frame, subtotal):
  print()
  print("**** {} Costs ****".format(heading))
  print(frame)
  print()
  print ("{} Costs: ${:.2f}".format(heading, subtotal))
  return ""
\

def profit_goal (total_costs):
  
  # Initialise variables and error message 
  error = "Please enter a valid profit goal \n"
  
  valid = False
  while not valid:
  
      # Ask for profit goal 
    response = input ("What is your profit goal (eg $500 or 50%) ")
  
    # Check if first character is $
    if response[0] == '$':
      profit_type = "$"
      # Get amount (everything after the $)
      amount = response[1:]
      
    elif response [-1] == "%":
      profit_type = "%"
      # Get amount (everything before the %)
      amount = response[:-1]
  
    else:
      # Set response to amount for now
      profit_type = "unknown"
      amount = response 
  
    try: 
      # Checks amoint is a nummber more than zero..
      amount = float (amount)
      if amount <= 0: 
        print (error)
        continue 
  
    except ValueError:
      print (error)
      continue 
  
    if profit_type == "unknown" and amount >= 100: 
      dollar_type = yes_no("Do you mean ${:.2f}. ie {:.2f} dollars? y / n".format(amount, amount))
  
      # Set profit type based on user answer above
      if dollar_type =="yes": 
        profit_type = "$"
      else: 
        profit_type = "%"
  
    elif profit_type == "unknown" and amount <100: 
      percent_type = yes_no("Do you mean {}%? , y / n: ".format(amount))
      if percent_type == "yes": 
        profit_type = "%"
      else: 
        profit_type = "$"
        
    # Return profit goal to main routine 
    if profit_type == "$": 
      return amount 
    else: 
      goal = (amount / 100) * total_costs
      return goal 



\

# Rounding function 
def round_up(amount, round_to):
  return int(math.ceil(amount / round_to)) * round_to
\

# **** MAIN ROUTINE GOES HERE ****

# Get product name
product_name = not_blank("Product name: ", "The product name cant't be blank")

how_many = num_checker("How many items will you be producing? The number of items must be more than zero", int)

print()
print("Please enter your variable costs below... ")
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
  fixed_sub = 0

# Works out total costs and profit target
all_costs = variable_sub + fixed_sub 
profit_target = profit_goal(all_costs)

# Calculates total sales needed to reach goal 
sales_needed = all_costs + profit_target

# Ask user for rounding 
nearest_dollar = num_checker("Round to the nearest...? $", int)
  
# un-rounded sales price
rrp_raw = sales_needed / how_many
rrp = round_up(rrp_raw, nearest_dollar)

# Write data to file

# Change dataframe to string
variable_txt = pandas.DataFrame.to_string(variable_frame)

if have_fixed == "yes":
  fixed_txt = pandas.DataFrame.to_string(fixed_frame)
else:
  fixed_txt = ""

product_str = "\n***** {} *****".format(product_name)
var_cost_heading = "\n----- Variable Costs -----"
var_cost_sub_str = "Variable Sub Total: ${:.2f}".format(variable_sub)
fixed_cost_heading = "--- Fixed Costs---"
sales_advice_heading = " --- Sales Advice --- "


profit_target_str = "Profit Target: ${:.2f}".format(profit_target)
required_sales_str = "Required Sales: ${:.2f}".format(sales_needed)
rrp_str = "*** Recommended Price: ${:.2f} ***".format(rrp)

# list holding stuff to print / write file
to_write = [product_str, var_cost_heading, variable_txt, var_cost_sub_str, fixed_cost_heading, fixed_txt, sales_advice_heading, profit_target_str, required_sales_str, rrp_str]

# Write to file .. 
# Create file to hold data add.txt extension
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# Heading 
for item in to_write: 
  text_file.write(item)
  text_file.write("\n\n")


# Close file 
text_file.close()

# Print stuff 
for item in to_write: 
  print(item)
  print()

# # *** Printing area *** 

# print()
# print("**** Fund Raising **** - {} *****".format(product_name))
# print()
# expense_print("Variable", variable_frame, variable_sub)

# if have_fixed == "yes": 
#   expense_print("Fixed", fixed_frame [['Cost']], fixed_sub)

# print()
# print("**** Total Costs: ${:.2f} ****".format(all_costs))
# print()

# print()
# print("**** Profit & Sales Targets ****")
# print("Profit Target: ${:.2f}".format(profit_target))
# print("Total Sales: ${:.2f}".format(all_costs + profit_target))


# print("**** Variable Costs ****")
# print(variable_frame)
# print()

# print ("Variable Costs: ${:.2f}".format(variable_sub))

# print()
# print("**** Recommended Selling price: ${:.2f}".format(selling_price))