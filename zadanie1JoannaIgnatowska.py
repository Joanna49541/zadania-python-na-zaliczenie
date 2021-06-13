import os

class Ksiazka:
    tytuł = ""
    autor = ""
    cena = ""
    
    def __init__(self, tytuł, autor, cena):
        self.tytul = tytuł
        self.autor = autor
        self.cena = cena

    def dodaj_ksiazke(self):
        tytul = "Tytuł" + self.tytuł + ' n\ '
        autor = "autor" + self.autor + " n\ " 
        cena = "cena" + self.cena + " n\ " 
        nowaKsiazka = Ksiazka(tytul, autor,cena)
        self.bazaKsiazek.append(nowaKsiazka)
    
    def usun_ksizke(self):
        self.bazaKsiazek.remove()

    def modyfikuj(self, nowyTytul, nowyAutor, nowaCena):
        self.tytul = nowyTytul
        self.autor = nowyAutor
        self.cena = nowaCena
        modyfikowanaKsiazka = Ksiazka(nowyTytul, nowyAutor, nowaCena)
        self.bazaKsiazek.append(modyfikowanaKsiazka)
    
    def wyswietl(self):
        for i in self.bazaKsiazek:
            print(Ksiazka)

    def zapisz_do_pliku(self, myfile):      
        myfile = open("C:\Users\Kura\Desktop\bazaKsiazek.odt", "w")
        myfile.write("bazaKsiazek[]")

    def doczytaj_z_pliku(self,myfile):
        myfile = open("C:\Users\Kura\Desktop\bazaKsiazek.odt", "r") 
        for line in myfile:
            print(line)   


bazaKsiazek = []


wybor = print("Wybierz aktywność: 1 - dodaj notatke, 2 - usun notatke, 3 - modyfikuj, 4 - wyswietl, 5 - zapisz do pliku, 6 - odczytaj z pliku, 0 - zakoncz  ")
while wybor != 0:
    i = input()
    if i == "0":
        break
    elif i == "1":
        Ksiazka.dodaj_ksiazke()
    elif i == "2":
        Ksiazka.usun_ksizke()  
    elif i == "3":
        Ksiazka.modyfikuj()
    elif i == "4":
        Ksiazka.wyswiel()
    elif i == "5":
        Ksiazka.zapisz_do_pliku()
    elif i == "6":
        Ksiazka.doczytaj_z_pliku()      





