from User import User
class Category:
    name: str
    desc: str
    author: User
    def __init__(self, name, desc, author):
        self.name = name
        self.desc = desc
        self.author = author

