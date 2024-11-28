"""
Created on Nov 28 2024

@author: Fisissist
"""
#************* Exercise 3 *************
print("Exercise 3")
sh = input('Enter hours: ') 
sr = input('Enter rate: ') 

# integers to float
fh = float(sh)
fr = float(sr)
print("Hours:",fh,"Rate:",fr)

if fh > 40:
	print("Overtime")
	reg = fr * fh # regular pay
	otp = (fh - 40) * (fr * 0.5) # overtime pay, hours over by half the rate
	print("Regular pay is",reg,"and overtime bonus pay is",otp)
	xp = reg + otp
else:
	print('Regular')
	xp = fh * fr
print("Pay:",xp)

#************* Exercise 4 *************
print("Exercise 4")

sh = input('Enter hours: ') 
sr = input('Enter rate: ') 

try: # if a string is entered then this will run the code
	fh = float(sh)
	fr = float(sr)
except:
	print('Error, enter numerical value.')
	quit() # terminates the try once it is run

if fh > 40:
	print("Overtime")
	reg = fr * fh 
	otp = (fh - 40) * (fr * 0.5)
	print("Regular pay is",reg,"and overtime bonus pay is",otp)
	xp = reg + otp
else:
	print('Regular')
	xp = fh * fr
print("Pay:",xp)
