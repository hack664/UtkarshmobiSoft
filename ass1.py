
marker = "----------------------------------------------------------------------------------------------"


print(marker)
print("<--- 1] Reverse a String and print it on console --->")

rev = "Python Skills"

print("printing reverse of Python Skills : ", rev[::-1])

print(marker)
print("<--- 2] Assign String to variable x as DD-MM-YYYY  and print Year --->")

x = "19:08:2021  ---> DD-MM-YYYY Format"
print("19:08:2021")
print("Printing Year from above String : ",x[6:10])

print(marker)
print("<--- 3] In a small company the average salary of three employees is Rs 1000 per week if one employee earns Rs1100 and other earns Rs 500 , how much the third employee earn ? ---> ")

print("note per 3 employee salary for one week is 1000 so 1000 x 3 = 3000")

emp3 = 3000-1100-500

print("the salary for third employee will be : ",emp3)

print(marker)
print("<--- 4] Write Program - Convert a Percentage to a Fraction --->")

n = 30/100

dec = n * 100

print("Decimal equivalent in %")

print(round(dec,2))

print(marker)
print("<--- 5] Write Program - A Train 340 m long is running at a speed of 45 km/hr. what time will it take to cross a 160 m long tunnel ? --->")

tunnel = 160

s = 45
speed = 45000/3600
distance = 340+160

time = distance/speed

print("time required to cross a tunnel is ",time)


print(marker)

print("--------------------------- End Of Assignment No 1 ---------------------------")