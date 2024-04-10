from datetime import datetime, timedelta

# Get the current date and time
current_date = datetime.now()

# Subtract five days from the current date
new_date = current_date - timedelta(days=5)

# Print the results
print("Current Date and Time:", current_date)
print("Current Date - 5 days:", new_date)


#import datetime

#x = datetime.datetime.now()

#print(x.year)
#print(x.strftime("%A"))