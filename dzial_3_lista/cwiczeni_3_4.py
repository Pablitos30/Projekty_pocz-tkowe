lista_gosci = ['Dorota','Justyna','Marta']
print(f"Serdecznie chciałbym zaprosić cię {lista_gosci[0]} Na obiad.")
print(f"Serdecznie chciałbym zaprosić cię {lista_gosci[1]} Na obiad.")
print(f"Serdecznie chciałbym zaprosić cię {lista_gosci[2]} Na obiad.")
# skrócona wersja

for names in lista_gosci:
    print(f"Serdecznie zapraszam cię {names} na obiad")


# wyświetlenie listy gości i kogo nie będzie na obiedzie.
lista_gosci = ['Dorota','Justyna','Marta']
print(lista_gosci)
nieobecny = lista_gosci.pop(1)
print(f"{nieobecny} - Tej osoby niestety nie bedzie na obiedzie.") 
print(lista_gosci) 
#Zstąpienie nowej osoby
lista_gosci.append('Ewa')
print(f"Ewa dołącza zmiast Justyny")
print(lista_gosci)
# Zaproszenie każdej z osobna
for names in lista_gosci:
    print(f"Serdecznie zapraszam cię {names} na obiad")

# Umieszczam polecenie o znalezieniu nowego stołu 
print("Właśnie znalazłem większy stół Super ! zaproszę więcej gości")
#wyświetlam aktualną listę gości i dodaje nowego gościa na początku listy za pomocą metody insert
print(lista_gosci)
lista_gosci.insert(0, 'Adrian')
# Za pomoca metody insert dodaje gościa w środku listy
lista_gosci.insert(1, 'Maciek')
# Za pomoćą metody append dodaje gościa na koncu listy 
lista_gosci.append('Jan')
#Wyswietlam nową listę gości
print(lista_gosci)
# Wyswietlam komunikat do kazdego z osobna dla kazdej osoby 
for names in lista_gosci:
    print(f"Serdecznie zapraszam cię {names} na obiad po południu.")

#stół nie zostanie dostarczony na czas
print("Przepraszam ale stół nie zostanie dostarczony na czas i mogę zaprosić tylko dwie osoby")
#  wyświetlam listę gości i za pomocą metody pop usuwam po jednym gościu z listy
print(lista_gosci)
print(f"{lista_gosci.pop(-1)}, przepraszam ale nie mogę zaprosić cię na obiad.")  # Jan
print(f"{lista_gosci.pop(-1)}, przepraszam ale nie mogę zaprosić cię na obiad.")  # Ewa
print(f"{lista_gosci.pop(-1)}, przepraszam ale nie mogę zaprosić cię na obiad.")  # Marta
print(f"{lista_gosci.pop(-1)}, przepraszam ale nie mogę zaprosić cię na obiad.")  # Dorota
#usuwam dwóch ostatnich gości z listy
del lista_gosci[0]
# już usunęło jedną pozycję z listy i teraz pozostała tylko jedna którą też usuwasz
del lista_gosci[0]
#sprawdzam czy lista jest pusta
print(lista_gosci)
#mozemy tez spróbowac wersji ze zmienną
#lista_gosci = ['Adrian','Maciek','Dorota','Marta','Ewa','Jan']
#usuwam ostatniego
#removed_guest_one = lista_gosci.pop(-1)
#print(f"{removed_guest_one}, przepraszam ale nie mogę zaprosić cię na obiad.")
#usuwam kolejnego
#removed_guest_two = lista_gosci.pop(-1)
#print(f"{removed_guest_two}, przepraszam ale nie mogę zaprosić cię na obiad.")


#Wersja z pętlą while
#Usuwamy gości, dopóki na liście zostanie tylko dwóch:
#lista_gosci = ['Adrian','Maciek','Dorota','Marta','Ewa','Jan']
#print("Przepraszam, ale mogę zaprosić tylko dwie osoby.\n")
# dopóki lista ma więcej niż 2 osoby...
#while len(lista_gosci) > 2:
#    removed_guest = lista_gosci.pop(-1)  # zdejmujemy ostatniego
#    print(f"{removed_guest}, przepraszam ale nie mogę zaprosić cię na obiad.")

#print("\nPozostali goście:")
#for guest in lista_gosci:
#    print(f"{guest}, zapraszam cię na obiad.")




 
