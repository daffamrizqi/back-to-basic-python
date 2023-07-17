"""
A metaclass is the class of a class. A class defines how an instance of the class behaves
while a metaclass defines how a class behaves. A CLASS IS AN INSTANCE OF A METACLASS.

type is the usual metaclass in Python. type itself a class, and it is its own type.
You won't be able to recreate something like type purely in python, but python cheats a little.
To create your own metaclass in Python you really just want to subclass type.

A metalass is most commonly used as a class-factory. When you create an object by calling
the class, Python creates a new class (when it executes the 'class' statement) by calling metaclass.

Combined with the normal __init__ and __new__ methods, metaclasses therefore
allow you to do 'extra things' when creating a class, like registering the new class
with some registry or replace the class with something else entirely

When the class statement is executed, Python first executes the body of the class
statement as a normal block of code.

In most langs, classes are just a pices of code that describe how to produce an object
"""


# In most langs, classes are just a pices of code that describe how to produce an object
class ObjectCreator(object):
    pass

my_object = ObjectCreator()
print(my_object)


"""
But classes are more than that in Python. CLASSES ARE OBJECTS TOO.
When a Python script runs, every line of code is executed from top to bottom.
When the python interpreter encounters the class keyword, Python creates an object
out of 'description' of the class that follows.
"""

"""
type can create classes on the fly. type can take the description of a class as parameters,
and return a class.
"""

# type works this way:
# type (name, bases, attrs)

"""
where:
name: name of the class
bases: tuple of the parent class (for inheritance, can be empty)
attrs: dictionary containing attributes names and values

for ie: code below
"""

# class MyShinyClass(object):
#     pass
# can be translated to:
MyShinyClass = type("MyShinyClass", (), {}) # returns a class object
print(MyShinyClass)
print(MyShinyClass()) # create an instance with the class

# another example:
class Foo(object):
    bar = True
Foo = type('FOO', (), {'bar': True})
print(f"\nIni foo: {Foo}")
print(f"\nIni instancenya: {Foo()}")


"""
WHAT ARE METACLASSES:

Metaclass are the 'stuff' that creates classes.
You define classes in order to create
"""
