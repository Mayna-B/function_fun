# arb_args - Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
  for a in args:
    print(a)

#Example Usage: 
# arb_args("Hello", "World", 123, [1, 2, 3])



# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(x,y):
  def inner_1():
    return x+y
  def inner_2():
    return x-y
  print(inner_1()+inner_2())

# Example Usage: 
# inner_func(10, 5)



# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(name, lunch="Mystery Meat"):
  print(name, lunch)

# Example Usage: 
# lunch_lady("Alice", "Pizza")
# lunch_lady("Bob")



# sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(x,y):
  return x+y,x*y

#Example Usage: 
# num1 = 5
# num2 = 3
# sum_value, product_value = sum_n_product(num1, num2)
# print(f"Sum: {sum_value}")
# print(f"Product: {product_value}")



# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.

alias_arb_args = arb_args

# Example Usage: 
# alias_arb_args("Hello", "World", 123, [1, 2, 3])



# arb_mean - Accepts any number of integers and prints their average.

def arb_mean(*args):
    total = 0
    for a in args:
        total += a
    print(total/len(args))

# Example Usage: 
# arb_mean(5, 10, 15)
# # arb_mean(2, 4, 6, 8, 10)



# arb_longest_string - Accepts any number of strings and returns the longest one.

def arb_longest_string(*args):
  long = 0
  longest = ""
  for a in args:
    if len(a) > long:
      long = len(a)
      longest = a
  return longest

# Example Usage: 
# longest_string = arb_longest_string("apple", "banana", "kiwi", "orange")
# print(f"The longest string is: {longest_string}")