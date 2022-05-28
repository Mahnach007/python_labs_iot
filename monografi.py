from publications import Publications

class Monografi(Publications):
    
    def __init__(self, publications_type: str, year: int, number_of_pages: int, name: str, price: int,  topic: str, monografi_type: str ):
        super().__init__(publications_type, year, number_of_pages, name, price)
        self.topic = topic
        self.monografi_type = monografi_type

    def __str__(self) -> str:
        return super().__str__() + f"Topic: {self.topic}, Type: {self.monografi_type}, Price: {self.price}, Year: {self.year}, Publication Type: {self.publications_type}, Name: {self.name}"