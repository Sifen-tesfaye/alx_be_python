from datetime import datetime, timedelta # import what we need
# display current date and time 
def display_current_datetime():
   current_date = datetime.now()
   print("current date and time :", current_date.strftime("%Y-%m-%d %HP:%M:%S"))
# calculate future date
def calculate_future_date():
   try:
      days = int(input("Enter the number of days to add to the current date :")
      future_date + datetime.now() + timedelta(days=days)
      print("Future date : ", future_date.strftime("%Y-%m-%d"))
   except valueError:
      print("please Enter a valid integer. ")
# run both functions
display_current_datetime()
calculate_future_date()
