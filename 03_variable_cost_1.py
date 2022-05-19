import pandas 

def num_checker (question, num_type):
  vaild = False 
  while not vaild:

  # ask user for number and check it is valid 
    try: 

      if num_type == "int":
        response = int(input (question))
        error = "Please enter a whole number over 0"
      else:
        response = float(input(question))
        error = "Please enter a whole number over 0"
  
      if response > 0:
         return response
      else:
         print(error)
      
        # if an interger is not entered, display and error 
    except ValueError: 
      print (error)

# Main routine goes here 
get_in = num_checker ("How many do you need? Please enter an amount more then 0: ", "int")

get_costs = num_checker ("How much does it cost? $ Please enter a number more then 0: ", "float")

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

# Main routine goes here 

# set up dictionaries and lists 

item_list = []
quantity_list = []
price_list = []

variable_dict = {
  "Item": item_list, 
  "Quantity": quantity_list, 
  "Price": price_list
}

# Get user data 
product_name = not_blank("Product name: ", "The product name cant't be blank")

# Loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

  print ()
  # Get name, quantity and item
  item_name = not_blank (" Item name: ", "The compopnent name can't be blanket.")
  if item_name.lower() == "xxx":
    break
  
  quantity = num_checker("Quantity: ", "The amount must be a whole number more than zero", )
  
  price = num_checker("How much for a single item? $", "The price must be a number <more than 0>", )

  # Add item, quantity and price to lists 
  item_list.append(item_name)
  quantity_list.append(quantity)
  price_list.append(price)

variable_frame = pandas.DataFrame (variable_dict)
variable_frame = variable_frame.set_index('Item')

# Calculate cost of each component 
variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame ['Price']

# Find sub total
variable_sub = variable_frame ['Cost'].sum ()

# Currency formatting (uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars: 
  variable_frame[item] = variable_frame[item].apply(currency)

# *** Printing area *** 

print(variable_frame)

print()

print ("variable Costs: ${:.2f}".format (variable_sub))