from modules.library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, isbn, authors, title, subject, dds_number, upc):
        LibraryItem.__init__(self, title, upc, subject)
        self.isbn = isbn
        self.authors = authors
        self.dds_number = dds_number

