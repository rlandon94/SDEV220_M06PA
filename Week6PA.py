from datetime import date, datetime

# Get the current date as a string
current_date = date.today().strftime('%Y-%m-%d')

# Write the date to the text file
with open('today.txt', 'w') as file:
    file.write(current_date)

print(f"Current date ({current_date}) has been written to today.txt.")

# Read the contents of the "today.txt" file into a string
with open('today.txt', 'r') as file:
    today_string = file.read()

print(f"Contents of today.txt: {today_string}")

# Parse the date from today_string
try:
    parsed_date = datetime.strptime(today_string, '%Y-%m-%d')
    print(f"Parsed Date: {parsed_date.strftime('%Y-%m-%d')}")
except ValueError:
    print("Invalid date format in today_string.")