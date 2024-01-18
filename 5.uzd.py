savs_vards=input("Ievadi savu vārdu: ")

with open("5.uzd.txt", "w", encoding='utf8') as kakis:
    kakis.write(savs_vards)


