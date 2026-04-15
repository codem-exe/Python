#Match-Case Statement (switch): An alternative to using many 'elif' statements
#                               Execute some if a value matches a 'case'
#                               Benefits: Cleaner and Syntax is more readable


def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"

print(day_of_week(1))