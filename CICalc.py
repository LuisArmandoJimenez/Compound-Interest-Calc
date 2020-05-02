# Compound Interest Calculator

"""
Equation to calculate compound interest
A = P (1 + (r/n))^nt
where:
A = final amount
P = initial principle amount
r = interest rate
n = # of times interest applied per time period
t = # of time periods
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import locale
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.disable(logging.CRITICAL)

locale.setlocale(locale.LC_ALL, "en_US.UTF8")

logging.debug("Start of program")

print("What is the starting principle?")
p = input()
pconv = locale.localeconv()
p_raw = p.strip(pconv["currency_symbol"])
p_str = locale.atof(p_raw)
P = int(p_str)


print("What is the % interest rate?")
percent = int(float(input()))
r = percent / 100

print("What is the number of times per year that interest is applied?")
n = int(input())

print("How many years will interest rate compound?")
t = int(input())

logging.debug("calculating interest earned")

A = (P * (1 + (r/n))**(n*t))
logging.debug("A is %s, r is %s" % (A, r))

logging.debug("calculating total")

# convert A to $ format
Total = "{0:,.2f}".format(A)

print("The final amount after " + str(t) + " years:")

print("$" + Total)

"""
Plot with x-axis as time in terms of years (e.g. 1, 2, 3 ...)
plot with y-axis as the amount at the end of the year in terms of $
The x-axis can be considered as years from 0 to t
the y-axis will be composed of $ and each bar will max out at A for the given t
"""
# x and y parameters
x = np.array(range(t))
y = (P * (1 + (r/n))**(n*x))

# create plot
plot = plt.plot(x, y)

# add titles and axes
plt.title("Compound Interest on Starting Principle Over " + str(t)+ " Years")
plt.xlabel("time (years)")
plt.ylabel("Total Amount ($)")
#yformat = matplotlib.ticker.StrMethodFormatter("${0:,.2f}")


#plot.yaxis.set_major_formatter(yformat)

# add grid
plt.grid(alpha = 0.5, linestyle = "dotted")

# show plot
plt.show()

logging.debug("End of program")
