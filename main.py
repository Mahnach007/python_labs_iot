
from book import Book
from magazine import Magazine
from monografi import Monografi



def main():

    marvel_book = Book("Book", 2020, 561, "Marvel", 20, "Printed", "Adventure", "Marvel Studious" )
    maxim_magazine = Magazine("Magazine", 2022, 56, "Maxim", 400, "18+", "Maxim Corp.")
    pythics_monografi = Monografi("Monografi", 1999, 123, "Ivan Styp", 10, "Pythics", "Educational")
    print(marvel_book,"\n", maxim_magazine,"\n", pythics_monografi)

if __name__ == '__main__':
    main()
