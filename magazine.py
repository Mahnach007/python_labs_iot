from publications import Publications


class Magazine(Publications):

    def __init__(self, publications_type: str, year: int, number_of_pages: int, name: str, price: int, magazine_type: str, name_of_edition: str):
        super().__init__(publications_type, year, number_of_pages, name, price)
        self.magazine_type = magazine_type
        self.name_of_edition = name_of_edition

    def __str__(self) -> str:
        return super().__str__() + "Type: {0}, Edition: {1}".format(self.magazine_type, self.name_of_edition)