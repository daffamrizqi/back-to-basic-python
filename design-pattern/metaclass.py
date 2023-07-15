"""
Metaclass adalah sebuah konsep yang memungkinkan kita untuk memanipulasi pembuatan kelas.
Kita bisa menganggap metaclass sebagai "class untuk membuat class". Dengan menggunakan
metaclass, kita bisa MENGONTROL CARA KELAS DIBUAT, termasuk prperti, metode dan perilaku nya
"""

class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        # Modifikasi atribut atau perilaku kelas sebelum dibuat
        attrs["my_variable"] = 123
        attrs["my_method"] = lambda self: print("Hello from my_method")

        return super().__new__(cls, name, bases, attrs)
    
class MyClass(metaclass=MetaClass):
    pass

some_obj = MyClass()
print(some_obj.my_variable) # Output: 123
some_obj.my_method() # Output: Hello from my_method!


"""
Metaclass dapat digunakan untuk melakukan modifikasi yang kompleks pada CLASS SAAT PEMBUATAN,
seperti pengecekan atribut, penambahan dekorator, atau penggantian perilaku secara dinamis.
"""