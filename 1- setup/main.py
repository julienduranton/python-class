

# My first command

print('Hello, World !')

# Quick intro to structures

my_array = [0,1,2,3,4,4,'five']

my_tuple = (1,2)

my_dict = {'id':1,
           'value':'one'}

my_set = {'one',2,3}

# get the first and last elements of the array

length_array = len(my_array)

first = my_array[0]
last = my_array[-1]
rest = my_array[1:len(my_array)-2]

my_array.append('six')

# Tuples are weird and I don't use them. You can't add values to it


# Dicts are practical and and array of dicts is essentially a classic spreadsheet where each dict is a row and each key is a column



my_keys = my_dict.keys()

# Add a new key,value pair to a dictionnary
my_dict['type'] = 'odd'


for key in my_keys:
  
  print('key:{}, value:{}'.format(key,my_dict.get(key)))
  print(my_dict[key])

# Sets are unordered, unindexed and unchangeable (but you can remove or add items) NO DUPLICATES

unique_array = list(set(my_array))

for item in my_set:
  if type(item) == str:
    print(item)

# My first program

def hello(input):
  output = 'Hello, {} !'.format(input)
  print(output)
  

hello("Sophie")
  
# My first loops

i = 0
while i < 10:
  print(i)
  i += 1


for i in range(10):
  print(i)
  
  
# Only even numbers

for i in range(10):
  if i % 2 == 0:
    print(i)
    
# function for odd number

def oddNumber(number):
  if number % 2 != 0:
    return True
  else:
    return False  


# function to return only odd numbers in an array

def oddArray(array):
  output = []
  for i in array:
    if oddNumber(i):
      output.append(i)
  return output

a = [i for i in range(100)]
res = oddArray(a)
print(res)        