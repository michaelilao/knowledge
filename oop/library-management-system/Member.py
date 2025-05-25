class Member():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()
