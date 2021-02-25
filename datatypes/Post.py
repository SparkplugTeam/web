from datatypes.User import User
from datatypes.Category import Category


class Post:
    user: User
    cat: Category
    title: str
    content: str

    def __init__(self, user, cat, title, content):
        self.user = user
        self.cat = cat
        self.title = title
        self.content = content

    def renderPost(self):
        return (
            self.title
            + "<br>"
            + "from "
            + self.user.username
            + ", in "
            + self.cat.name
            + "<br>"
            + self.content
        )
