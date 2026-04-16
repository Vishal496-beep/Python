# Python
mutable and immutable

mutable -> jo change ho skt hai
immutable -> jo change nhi ho skta h
example->
username = "vishal"
output - vishal
username = 'chai'
output - > chai
now value is changing in username but it is storing string but the main thing is in memory the thing that is immutable is value in string meaning 'visha' and 'chai' are immutable rather than username =>
ab kyuki jo username m 2nd value means reference chai ka de diya tha toh isliye username m value chai aayegi or jo vishal value thi use  reference dene k liye koi nhi h toh woh automatically will be transfered on garbage collection
->thats what immutable and mutable are
// Mutable data types are those that can be changed after they are created, while immutable data types cannot be changed after they are created. In Python, examples of mutable data types include lists, dictionaries, and sets, while examples of immutable data types include strings, tuples, and frozensets. Understanding the difference between mutable and immutable data types is important for writing efficient and effective code in Python.
python m datatype nhi hota but memory m hota h string number dict list tuple set etc. ye sab data types h jo memory m store hote h but python m datatype nhi hota h

// In Python, there are no explicit data types like in other programming languages. However, Python does have built-in data structures such as strings, numbers, dictionaries, lists, tuples, and sets that are stored in memory. These data structures can be mutable or immutable, depending on whether they can be changed after they are created. Understanding the difference between mutable and immutable data types is important for writing efficient and effective code in Python.

# Mutable data types
 in Python include lists, dictionaries, and sets. These data types can be modified after they are created, meaning you can add, remove, or change elements within them. For example, you can append an item to a list or update a value in a dictionary.

# Immutable data types
 in Python include strings, tuples, and frozensets. These data types cannot be modified after they are created, meaning you cannot change their contents. For example, you cannot change a character in a string or add an item to a tuple.

# Understanding the difference 
between mutable and immutable data types is important for writing efficient and effective code in Python. Mutable data types can be useful when you need to modify data, while immutable data types can help ensure that your data remains unchanged and can be safely shared across different parts of your code.

is = operator -> it is used to compare the memory location of two objects. It returns True if both operands refer to the same object in memory, and False otherwise.  is m = n and m is n theres a difference between them. m = n is an assignment statement that assigns the value of n to m, while m is n is a comparison statement that checks if m and n refer to the same object in memory. For example:   m = [1, 2, 3]
n = m   
print(m is n)  # Output: True
In this example, m and n refer to the same list object in memory, so m is n returns True. However, if we create a new list with the same contents, it will not be the same object in memory:   m = [1, 2, 3]
n = [1, 2, 3]
print(m is n)  # Output: False


Numbers -> its a group of immutable data types in Python that represent numeric values. There are several types of numbers in Python, including integers, floating-point numbers, and complex numbers. Integers are whole numbers without a decimal point, while floating-point numbers are numbers with a decimal point. Complex numbers consist of a real part and an imaginary part. Understanding the different types of numbers in Python is important for performing mathematical operations and working with numerical data effectively.

set -> its a built-in data type in Python that represents an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from a set after it is created. Sets are useful for performing mathematical operations such as union, intersection, and difference, as well as for removing duplicates from a list. Understanding how to use sets in Python can help you write more efficient and effective code when working with collections of data.


# Strings 
-> its a built-in data type in Python that represents a sequence of characters. Strings are immutable, meaning you cannot change the contents of a string after it is created. Strings can be created using single quotes, double quotes, or triple quotes. They can also be concatenated using the + operator and repeated using the * operator. Understanding how to work with strings in Python is important for manipulating text data and performing various operations such as slicing, formatting, and searching.

# slice -> 
its a technique in Python that allows you to extract a portion of a sequence, such as a string, list, or tuple. The slice syntax uses the colon (:) operator to specify the start and end indices of the slice. For example, my_string[0:5] would return the first five characters of the string my_string. Slicing can also be used with negative indices to extract elements from the end of a sequence. Understanding how to use slicing in Python is important for manipulating and extracting data from sequences effectively.

# split -> 
its a method in Python that allows you to divide a string into a list of substrings based on a specified delimiter. For example, my_string.split(',') would return a list of substrings separated by commas. Understanding how to use the split method in Python is important for manipulating and processing text data effectively.
# join ->
its a method in Python that allows you to concatenate a list of strings into a single string,       using a specified delimiter. For example, ','.join(my_list) would return a single string with the elements of my_list separated by commas. Understanding how to use the join method in Python is important for manipulating and processing text data effectively.

# replace 
-> its a method in Python that allows you to replace occurrences of a specified substring with another substring in a string. For example, my_string.replace('old', 'new') would return a new string with all occurrences of 'old' replaced with 'new'. Understanding how to use the replace method in Python is important for manipulating and processing text data effectively.

# list 
-> its a built-in data type in Python that represents an ordered collection of elements. Lists are mutable, meaning you can add, remove, or change elements in a list after it is created. Lists can contain elements of different data types, including other lists. Understanding how to work with lists in Python is important for manipulating and processing collections of data effectively.


# list 
-> its a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, such as a list or range. The syntax for list comprehension is [expression for item in iterable if condition], where the expression is evaluated for each item in the iterable that satisfies the condition. List comprehensions can make your code more readable and efficient when creating new lists based on existing data.

# insert
 -> its a method in Python that allows you to insert an element at a specific index in a list. The syntax for the insert method is list.insert(index, element), where index is the position where you want to insert the element and element is the value you want to insert. Understanding how to use the insert method in Python is important for manipulating and processing lists effectively.

 # remove
 -> its a method in Python that allows you to remove the first occurrence of a specified element from a list. The syntax for the remove method is list.remove(element), where element is the value you want to remove. Understanding how to use the remove method in Python is important for manipulating and processing lists effectively.
# pop
    -> its a method in Python that allows you to remove and return an element from a list at a specified index. The syntax for the pop method is list.pop(index), where index is the position of the element you want to remove. If no index is specified, the pop method will remove and return the last element of the list. Understanding how to use the pop method in Python is important for manipulating and processing lists effectively.

# .copy
 -> its a method in Python that allows you to create a shallow copy of a list. The syntax for the copy method is list.copy(), where list is the original list you want to copy. A shallow copy creates a new list object, but the elements within the list are still references to the same objects in memory. Understanding how to use the copy method in Python is important for manipulating and processing lists effectively, especially when you want to avoid modifying the original list.

 # dictionary 
 -> its a built-in data type in Python that represents an unordered collection of key-value pairs. Dictionaries are mutable, meaning you can add, remove, or change key-value pairs in a dictionary after it is created. Keys in a dictionary must be unique and immutable, while values can be of any data type. Understanding how to work with dictionaries in Python is important for manipulating and processing collections of data effectively.

 # .get
 -> its a method in Python that allows you to retrieve the value associated with a specified key in a dictionary. The syntax for the get method is dictionary.get(key, default), where key is the key you want to retrieve the value for and default is an optional value that will be returned if the key is not found in the dictionary. Understanding how to use the get method in Python is important for manipulating and processing dictionaries effectively, especially when you want to avoid KeyError exceptions when trying to access keys that may not exist in the dictionary.

# for loop
 -> its a control flow statement in Python that allows you to iterate over a sequence of elements,      such as a list, tuple, or string. The syntax for a for loop is for variable in iterable: followed by an indented block of code that will be executed for each element in the iterable. For example, you can use a for loop to iterate over a list of numbers and print each number to the console. Understanding how to use for loops in Python is important for manipulating and processing collections of data effectively.

 # dictonary comprehension
 -> its a concise way to create dictionaries in Python. It allows you to generate a new dictionary by applying an expression to each item in an iterable, such as a list or range. The syntax for dictionary comprehension is {key_expression: value_expression for item in iterable if condition}, where key_expression is the expression that generates the keys, value_expression is the expression that generates the values, and condition is an optional filter that determines which items from the iterable are included in the resulting dictionary. Dictionary comprehensions can make your code more readable and efficient when creating new dictionaries based on existing data.

 # squared 
 -> its a mathematical operation that multiplies a number by itself. In Python, you can calculate the square of a number using the exponentiation operator (**). For example, to calculate the square of 5, you can use the expression 5 ** 2, which will return 25. Understanding how to calculate squares in Python is important for performing mathematical operations and working with numerical data effectively.

 # fromKeys
 -> its a method in Python that allows you to create a new dictionary from a sequence of keys, with a specified value for each key. The syntax for the fromkeys method is dict.fromkeys(keys, value), where keys is an iterable containing the keys for the new dictionary and value is the value that will be assigned to each key. If no value is specified, the default value will be None. Understanding how to use the fromkeys method in Python is important for creating dictionaries efficiently when you have a list of keys and want to assign a common value to them.

 # tuple
 -> its a built-in data type in Python that represents an ordered collection of elements. Tuples are immutable, meaning you cannot add, remove, or change elements in a tuple after it is created. Tuples can contain elements of different data types, including other tuples. Understanding how to work with tuples in Python is important for manipulating and processing collections of data effectively, especially when you want to ensure that the data remains unchanged throughout your code.

 # list and tuple m difference
-> The main difference between a list and a tuple in Python is that lists are mutable, while tuples are immutable. This means that you can modify a list by adding, removing, or changing elements, while you cannot modify a tuple after it is created. Additionally, lists are defined using square brackets [], while tuples are defined using parentheses (). Understanding the difference between lists and tuples is important for choosing the appropriate data structure for your needs and ensuring that your code behaves as expected when working with collections of data.

# __next__ 
-> its a special method in Python that is used to retrieve the next item from an iterator. When you call the next() function on an iterator, it internally calls the __next__() method to get the next item. If there are no more items to retrieve, the __next__() method raises a StopIteration exception. Understanding how to use the __next__() method in Python is important for working with iterators and creating custom iterable objects effectively.

# readline 
-> its a method in Python that allows you to read a single line from a file. The syntax for the readline method is file.readline(), where file is the file object you want to read from. Each time you call readline, it will return the next line from the file as a string, including the newline character at the end of the line. Understanding how to use the readline method in Python is important for working with files and processing text data effectively.
 
# function definition
-> its a block of reusable code in Python that performs a specific task. Functions are defined using    the def keyword, followed by the function name and parentheses that may contain parameters. The code block within the function is indented, and the function can return a value using the return statement. Understanding how to define and use functions in Python is important for organizing your code, improving readability, and promoting code reuse.

# polymorphism
-> its a programming concept that allows objects of different classes to be treated as objects of a common superclass. In Python, polymorphism is achieved through method overriding, where a subclass can provide its own implementation of a method that is already defined in its superclass. This allows you to use the same method name to perform different tasks based on the type of object that is calling the method. Understanding polymorphism in Python is important for writing flexible and extensible code that can work with different types of objects without needing to know their specific classes.

# lambda function
-> its a small anonymous function in Python that can have any number of arguments but can only have one expression. Lambda functions are defined using the lambda keyword, followed by the arguments and a colon, and then the expression that is evaluated and returned when the function is called. Lambda functions are often used for short, simple functions that are not intended to be reused elsewhere in the code. Understanding how to use lambda functions in Python can help you write more concise and efficient code when you need to create small, one-off functions.

# *args and **kwargs
-> *args and **kwargs are special syntax in Python that allow you to pass a variable number of arguments to a function. *args is used to pass a variable number of non-keyword arguments, while **kwargs is used to pass a variable number of keyword arguments. When you use *args in a function definition, it collects all the non-keyword arguments into a tuple. When you use **kwargs, it collects all the keyword arguments into a dictionary. Understanding how to use *args and **kwargs in Python is important for writing flexible functions that can handle different numbers and types of arguments effectively.
# Python

# yield 
its a keyword in Python that is used to create generator functions. A generator function is a special type of function that returns an iterator, which can be used to iterate over a sequence of values. When a generator function is called, it does not execute the function body immediately. Instead, it returns a generator object that can be iterated over using the next() function or a for loop. The yield keyword is used to produce a value from the generator function and pause its execution until the next value is requested. Understanding how to use yield in Python is important for creating efficient and memory-friendly code when working with large datasets or infinite sequences.

# namespaces
-> its a mapping of names to objects in Python. A namespace is created when a function is defined, and it contains all the names that are defined within that function. There are different types of namespaces in Python, including local, global, and built-in namespaces. The local namespace contains names that are defined within a function, while the global namespace contains names that are defined at the top level of a module or script. The built-in namespace contains names that are predefined by Python, such as built-in functions and exceptions. Understanding how namespaces work in Python is important for avoiding naming conflicts and ensuring that your code behaves as expected when accessing variables and functions.

# closures
-> its a programming concept in Python that allows a function to access variables from its enclosing scope, even after the outer function has finished executing. A closure is created when a nested function references a variable from its enclosing scope. The nested function retains access to the variable, allowing it to be used even after the outer function has returned. Closures are often used to create functions that have access to private variables or to implement decorators. Understanding closures in Python is important for writing more flexible and powerful code that can take advantage of the scoping rules of the language effectively.

# self
-> its a convention in Python to refer to the instance of a class. The self parameter is the first parameter of any method in a class and is automatically passed when an object of the class is created. It allows you to access and modify the attributes and methods of the instance within the class. Understanding how to use self in Python is important for writing object-oriented code that can create and manipulate instances of classes effectively. example class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(self.value)
my_object = MyClass(10)
my_object.display()  # Output: 10
this key in js is similar to self in python we can access the properties of an object using this in js and using self in python

# f"" strings
-> f"" strings (formatted string literals) are a way to embed expressions inside string literals in Python. They are prefixed with an 'f' and allow you to include expressions directly inside curly braces {}. The expressions are evaluated at runtime and their values are inserted into the string. This makes it easier to create dynamic strings without having to use concatenation or formatting methods. For example:
name = "Alice"  

# encapsulation
-> its a fundamental principle of object-oriented programming that restricts access to certain components of an object and prevents the accidental modification of data. In Python, encapsulation is achieved through the use of private and protected attributes and methods. Private attributes and methods are denoted by a double underscore prefix (e.g., __private_attr), while protected attributes and methods are denoted by a single underscore prefix (e.g., _protected_attr). By using encapsulation, you can ensure that the internal state of an object is hidden from external code and can only be accessed or modified through defined interfaces, which helps to maintain the integrity of the object and promotes better code organization.

# inheritance
-> its a fundamental principle of object-oriented programming that allows a new class (called a subclass or child class) to inherit properties and behaviors from an existing class (called a superclass or parent class). In Python, you can create a subclass by defining a new class that specifies the parent class in parentheses. The subclass can override or extend the functionality of the parent class by defining its own methods and attributes. Inheritance promotes code reuse and allows you to create a hierarchy of classes that share common features while still allowing for specialization. Understanding inheritance in Python is important for writing efficient and maintainable object-oriented code.

# polymorphism
 polymorphism is the ability of an object to take on many forms. It allows us to use a single interface to represent different types of objects. In Python, we can achieve polymorphism through method overriding and duck typing. 
 # static
    methods are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance (self) or class (cls) variables. Static methods are typically used for utility functions that do not require access to instance or class data. Understanding how to use static methods in Python is important for organizing your code and providing functionality that is related to the class but does not depend on instance-specific data.

# @staticmethod
 is a decorator in Python that is used to define a static method within a class. A static method is a method that belongs to the class rather than an instance of the class. It does not have access to the instance (self) or class (cls) variables and is typically used for utility functions that do not require access to instance or class data. To define a static method, you can use the @staticmethod decorator above the method definition. For example:
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")   

# @property
 is a built-in decorator in Python that allows you to define a method as a property of a class. A property is a special kind of attribute that is computed on-the-fly when accessed. By using the @property decorator, you can define a method that can be accessed like an attribute, without needing to call it as a function. This allows you to create read-only attributes or to perform additional processing when an attribute is accessed. For example:
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value  


# enumerate
 is a built-in function in Python that allows you to iterate over a sequence while keeping track of the index of the current item. It takes an iterable as an argument and returns an iterator that produces pairs of index and value for each item in the iterable. This is particularly useful when you need to access both the index and the value of items in a loop. For example:
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
