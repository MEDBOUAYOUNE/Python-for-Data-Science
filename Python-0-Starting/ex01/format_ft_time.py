from datetime import date
import time



seconds = time.time()
print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation$")

today = date.today()
today_formatted = today.strftime("%b %d %Y")
print(today_formatted)




# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)
# d1 = 27/12/2022

# d2 = today.strftime("%B %d, %Y")
# print("d2 =", d2)
# d2 = December 27, 2022

# d3 = today.strftime("%m/%d/%y")
# print("d3 =", d3)
# d3 = 12/27/22

# d4 = today.strftime("%b-%d-%Y")
# print("d4 =", d4)
# d4 = Dec-27-2022
