class Publications():

    acord = 12 

    def __init__(self, publications_type: str, year: int,  number_of_pages: int, name: str, price: int):
        
        self.publications_type = publications_type
        self.year = year
        self.price = price
        self.number_of_pages = number_of_pages
        self.name = name
   
   
    def __str__(self) -> str:
         return f"Type:{self.publications_type}, Year:{self.year}, Price:{self.price}, Pages:{self.number_of_pages}, Name: {self.name}"


""" def sort_by_price(o1: object):
        list_of_publications = []
        list_of_publications.append()
        list_of_publications.sort(price)"""