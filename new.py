class User:
    def __init__(self,name,birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        print(self.name.upper())

    def age(self,current_year):
        age = current_year - self.birthyear
        return age

while True:
    user = User(name="Ramya",birthyear=1999)
    user.get_name()
    user.age(current_year=2023)
