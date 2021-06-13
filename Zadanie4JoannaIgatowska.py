litery = input("Wypierowadź słowo: ")

litery.upper()
print(litery)

litera = []
for i in litery:
    litera.append(i)
    print(i)


counter = 0

for g in litera:
    if litera == "A" or litera == "E" or litera == "I" or litera == "N" or litera == "O" or litera == "R" or litera == "S" or litera == "W" or litera == "Z":
        counter += 1        
    elif litera == "C" or litera == "D" or litera == "K" or litera == "L" or litera == "M" or litera == "P" or litera == "T" or litera == "Y":
        counter += 2
    elif litera == "B" or litera == "G" or litera == "H" or litera == "J" or litera == "Ł" or litera == "U":
        counter += 3
    elif litera == "Ą" or litera == "Ę" or litera == "F" or litera == "Ó" or litera == "Ś" or litera == "Ż":
        counter += 5
    elif litera == "Ć": 
        counter += 6
    elif litera == "Ń":  
        counter += 7
    elif litera == "Ź":
        counter += 9

print("Twoje słowo ma:", counter )
            


