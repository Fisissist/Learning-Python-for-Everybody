"""
Created on Nov 28 2024

@author: Fisissist
"""
#************* Exercise 5 *************
print("Exercise 5")

def computepay(hours,rate): # defining the function
	print("In computepay",hours,"hours at a rate of",rate)
	if hours > 40:
		reg = rate * hours 
		otp = (hours - 40) * (rate * 0.5) 
		pay = reg + otp
	else:
		pay = hours * rate
	# print("Returning",pay)
	return pay # returns value of pay

sh = input('Enter hours: ') 
sr = input('Enter rate: ') 
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr) #calls function and give result


print("Pay:",xp)