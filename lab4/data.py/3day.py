from datetime import datetime, timedelta

# Get the current date and time
current_date = datetime.now()

# Calculate yesterday and tomorrow
yesterday_date = current_date - timedelta(days=1)
tomorrow_date = current_date + timedelta(days=1)

# Print the results
print("Yesterday:", yesterday_date.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow_date.strftime("%Y-%m-%d"))
