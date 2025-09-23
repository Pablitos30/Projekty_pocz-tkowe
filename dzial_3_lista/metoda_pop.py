#usuniecie ostatniego elementu z listy
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#komunikat o ostatnio zakupionym motocyklu

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"Ostatnio zakupiony przeze mnie motocykl to {last_owned.title()}.")

#usunięcie dowolnego elementu z listy

motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"Mój pierwszy motocykl to {first_owned.title()}.")

#przypomnienie
print("\t\nArek")

#metoda remove()

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#przyczyna usuniecia z listy motocykla

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nMotocykl {too_expensive.title()} jest zbyt drogi dla mnie.")
