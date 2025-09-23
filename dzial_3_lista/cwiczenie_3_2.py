#Przykła 1 błędny
names = ['Natalia','Kacper','Krystian','Karolina']
message_1 = f"Witaj jak się masz {names[0]}{names[1]}{names[2]}{names[3]}"
print(message_1)
#Przykład 2
names = ['Natalia', 'Kacper', 'Krystian', 'Karolina']
print(f"Witaj jak się masz {names[0]}?")
print(f"Witaj jak się masz {names[1]}?")
print(f"Witaj jak się masz {names[2]}?")
print(f"Witaj jak się masz {names[3]}?")
#Przykład 3 Pętla
names = ['Natalia', 'Kacper', 'Krystian', 'Karolina']
for name in names:
    print(f"Witaj jak się masz {name}?")

#Przykład 4 Join
names = ['Natalia', 'Kacper', 'Krystian', 'Karolina']
wszyscy = ", ".join(names)
print(f"Cześć {wszyscy}!")