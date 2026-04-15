import calendar

print("Python Calendar Viewer")


year = int(input("Enter the year (e.g., 2025): "))
month = int(input("Enter the month (1-12): "))


print("\nHere's your calendar:\n")
print(calendar.month(year, month))
