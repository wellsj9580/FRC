# Functions go here

# Check sthat the user has enetred yes / no to thye question 
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



costs = float(input("what are your costs? $"))
profit_needed = profit_goal(costs)
# print("we got to the end of the program")
print(profit_needed)
total = profit_needed + costs
print(total)