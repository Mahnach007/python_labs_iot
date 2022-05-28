from publications import Publications


class Book(Publications):

    def __init__(self, publications_type: str, year: int, number_of_pages: int, name: str, price: int, book_type: str, book_ganer: str, author: str ):
        super().__init__(publications_type, year, number_of_pages, name, price)
        self.book_type = book_type
        self.book_ganer = book_ganer
        self.author = author
        
    def __str__(self) -> str:
        return super().__str__() + "Type: {0}, Ganer: {1}, Author: {2}".format(self.book_type,self.book_ganer,self.author)

