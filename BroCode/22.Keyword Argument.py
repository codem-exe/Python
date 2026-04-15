#Keyword Argument = an argument preceded by an identifier
#                   helps with readability
#                   order of arguments doesn't matter
#                   1.Positional
#                   2.Default
#           --->    3.KEYWORD
#                   4.Arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="Bhattacharjee", first="Mainak")


# for x in range(1,11):
#     print(x, end=" ")


def phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = phone(country=91, area=123, first=456, last=7890)

print(phone_num)