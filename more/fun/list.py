# in this python app we are made convert to list method

# convert tuple to list with custom convert 
my_tuple = (1,2,3)

# bulit in python
# my_list_convert = list(my_tuple) 

my_new_list = []
for item in my_tuple:
    my_new_list.append(item)

print(my_new_list)
print(type(my_new_list))

