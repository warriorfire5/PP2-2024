import datetime

# Get the current date and time
current_date = datetime.now()

# Format the date without microseconds
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

# Print the result
print("Original Date and Time:", current_date)
print("Date and Time without Microseconds:", formatted_date)