#Data:

#Lists []
list_name = ['item1','item2']

#insert / append: add lists into a list
#extend: add variables from a list into a list
#remove to delete any item
#pop to remove last item (also returns it for setting the popped item as a variable)
#Count entries with len function : print(len(list_name))
#Use min or max or sum: print(list_name(min))
#Find entries with 'in':

print('item1' in list_name) #for true/false response
#or find key location with
print(list_name.index ('item1'))

#Loop through items in the list and show each index key starting with index number 1000:

for index, entries in enumerate(list_name, start=1000):
    print(index, entries)

#sorting:
reverse()
#ascending order:
sort()
#descending order:
sort(reverse=True)

#or sort and return list as new list but keep original list intact:
new_list = sorted(original_list)

#convert your list into a single string:
list_as_a_csv_string = ','.join(original_list)
#convert your csv into a list:
list = list_as_a_csv_string.split(',')

#Tuples ()
tuple_name = ('item1',item2)
#Same as list, but cannot modify (immutable)

#Sets {}
set_name = {'item1','item2'}

#Unordered collections of values with no duplicates
#The order will change each time you print
#Duplicates will not be shown when printing


#Membership test (can also do this with lists and tuples, but faster with sets)
print ('item_1' in set_name)

#Can find matching set data with intersection:
print (set_1.intersection(set_2))
#Can find non-matching data with difference:
print (set_1.difference(set_2))
#Can combine sets with union:
print(set_1.union(set_2))

#Dictionary{}:
set_name = {'attribute_1':'attribute_value', 'attribute_2':100,'list_1':['value_x', 'value_y])
#Sets can contain dictionary data - key/value pairs.

#Add new pairs with:
set_name['attribute_3'] = 'attribute_value'

#You can update pairs with:
set_name.update({'attribute_1':'new_attribute_value','attribute_2':101})

#You can delete pairs with:
del set_name['attribute_1]
#or
#pop off and set a new separate variable with:
attribute_1 = set_name.pop('attribute_1')

#You can retrieve these with
print (set_name['attribute_1'])
#or
print(set_name.get('attribute_1')

#View keys/values/both with this:
print(set_name.values())
print(set_name.keys())
print(set_name.item())

#Loop through and view each key pair:
for key,value in set_name.items():
print(key,value)

