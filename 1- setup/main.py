

# My first command

print('Hello, World !')


# My first program

def hello(input):
  output = 'Hello, {}'.format(input)
  print(output)
  
  
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