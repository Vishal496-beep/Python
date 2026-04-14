# we just created a form in car class
# class k ander hmesha self use krna kuch bhi access krne k liye 
# #encapsulation setting / getting private things only by accessing the whole structure we can get key and values 
# we took reference for electriccar as putting car in parenthesis
#we use super to access values in uppur means its known as inheritence
# the moment we put two underscores in two variables that variable becomes private
# polymorphism is the ability of an object to take on many forms. It allows us to use a single interface to represent different types of objects. In Python, we can achieve polymorphism through method overriding and duck typing. 
# 

## @staticmethod
#  is a decorator in Python that is used to define a static method within a class. A static method is a method that belongs to the class rather than an instance of the class. It does not have access to the instance (self) or class (cls) variables and is typically used for utility functions that do not require access to instance or class data. To define a static method, you can use the @staticmethod decorator above the method definition. For example:
# class MyClass:
#     @staticmethod
#     def static_method():
#         print("This is a static method.")   

# # @property
# it makes or makes sure that variable read only with no changes can be done
# #  is a built-in decorator in Python that allows you to define a method as a property of a class. A property is a special kind of attribute that is computed on-the-fly when accessed. By using the @property decorator, you can define a method that can be accessed like an attribute, without needing to call it as a function. This allows you to create read-only attributes or to perform additional processing when an attribute is accessed. For example:
# class MyClass:
#     def __init__(self, value):
#         self._value = value

#     @property
#     def value(self):
#         return self._value  

#isinstance() is a built-in function in Python that checks if an object is an instance of a specified class or a subclass thereof. It takes two arguments: the object to check and the class (or tuple of classes) to check against. The function returns True if the object is an instance of the specified class or any of its subclasses, and False otherwise. For example:
# class MyClass:
#     pass  

#multiple inheritance is a feature in object-oriented programming where a class can inherit attributes and methods from more than one parent class. This allows a child class to combine the functionality of multiple parent classes, which can be useful for creating complex objects that require features from different classes. In Python, you can achieve multiple inheritance by specifying multiple parent classes in the class definition. For example:
# class Parent1:    