# num1 = 10 
# num2 = num1

# print("Value of num1 ", num1 , id(num1))
# print ("value of num2" , num2 , id(num2))

# num2 = 22
# print("Value of num1 ", num1 , id(num1))
# print ("value of num2" , num2 , id(num2))

dict = {
    "age" : 11
}

dict1= dict

print("Value of dict ", dict , id(dict))
print ("value of dict1" , dict1 , id(dict1))

dict1["age"]=55
print("Value of dict ", dict , id(dict))
print ("value of dict1" , dict1 , id(dict1))
