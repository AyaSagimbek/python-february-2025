food=("burger", "pizza", "taco")
drink=("coke", "pepsi", "juice")

my_list=list(food)  #converting to list 
my_list.append("sushi") 
print(my_list) 

print(food)
print(drink)
print(food[1]) #indexing from the beginning
print(food[-1]) # "-"indexing from the end
print(drink[-2])

print(f"Can I have {food[0]} and {drink[1]}")