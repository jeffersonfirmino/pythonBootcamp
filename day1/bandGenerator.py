city= str(input("Whats the city that you grew up?"))
pet= str(input("Whats your pet name? "))
age = int(input("Whats your age? "))
band_name = city + pet 

print("Your band name is", band_name)

#another forms of print

print(f"Your band name is {city}{pet*2}") #including mathematical operations between the curly brackets

print("your band name is %s"%(band_name)) # if it has more values separate them with parenthesys and commas like this below
print("your band name is %s %s + %s"%(band_name,city,pet))

#or we can just simplily use concats

print("your band name is "+ city + pet)



# this form is capable to specify including decimal places.

print("Your age is %.2f" %age)
