"""
METHOD 1
"""
class GovSingleton:
    __instance__ = None

    def __init__(self):
        # constructor

        if GovSingleton.__instance__ is None:
            # assigning the current instance to this __instance__ variable
            GovSingleton.__instance__ = self
        else:
            raise Exception("We can not create another class")

    @staticmethod
    def get_instance():
        # We define the static method to fetch instance
        if not GovSingleton.__instance__:
            GovSingleton()
        return GovSingleton.__instance__


# creating an object of above defined class
gover = GovSingleton()
same_gover = GovSingleton.get_instance()
print(f"\nThis is the same gover: {same_gover}")

another_gover = GovSingleton.get_instance()
print(f"\nThis is another gover: {another_gover}")

new_gover = GovSingleton()
print(f"\nThis is new gover: {new_gover}")


"""
EXPLANATION:
- Above, we have instantiated an object and stored it in a variable.
- We have also defined construction, which checks if there is another existing class; otherwise,
  it will raise an exception
- We have then defined the static method named get_instance(),, which returns the existing instance
  ;  if it is not availabe, then create it and return
"""




"""
METHOD 2: Doubled check Locking Singleton Design Pattern
"""
