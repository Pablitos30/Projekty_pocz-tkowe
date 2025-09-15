imie_osoby = "aRek"
print(imie_osoby.lower())
print(imie_osoby.upper())
print(imie_osoby.title())

imie_osoby = input("Czy mógłbyś podać swoje imię ?: ")
print(
    f"Małe litery: {imie_osoby.lower()}\n"
    f"Wielkie litery: {imie_osoby.upper()}\n"
    f"Pierwsza litera wielka: {imie_osoby.title()}"
)