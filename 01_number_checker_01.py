# function goes here


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