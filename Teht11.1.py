class Publication:

    def __init__(self, name):
        self.name = name


class Book(Publication):

    def __init__(self, name, author, page_count):
        Publication.__init__(self, name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        print(f"Nimi: {self.name} \nKirjoittaja: {self.author} \nSivumäärä: {self.page_count} \n")


class Magazine(Publication):

    def __init__(self, name, editor):
        Publication.__init__(self, name)
        self.editor = editor

    def print_info(self):
        print(f"Nimi: {self.name} \nPäätoimittaja: {self.editor} \n")


aa = Magazine("Aku Ankka", "Aki hyyppä")
hytti = Book("Hytti n:o 6", "Rosa Liksom", 200)

aa.print_info()
hytti.print_info()