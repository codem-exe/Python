#default arguments = A default value for certain parameters
#                    The default is used when that argument is omitted
#                    make your function more flexible, reduces number of arguments
#                    1.positional,
#             --->   2.DEFAULT,
#                    3.keyword,
#                    4.Arbitrary


# def net_price (list_price, discount = 0, tax = 18):
#     return list_price * ( 1 - discount) * (1 + tax)
#
# print(net_price(500000,0.25))

import time

def count(end,start = 0):
    for x in range (start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(30,15)