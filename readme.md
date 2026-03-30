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
