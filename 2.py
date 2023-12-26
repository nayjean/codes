names = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")

    name = name[0:name.index(' ')].upper() + name[name.index(' '):].lower()

    if " " in name:
        name = name.replace(" ", "")

    if len(name) > 2:
        name = name[:-2]
    
    names.append(name)

n = len(names)
for i in range(n):
    for j in range(0, n-i-1):
        if names[j] > names[j+1]:
            names[j], names[j+1] = names[j+1], names[j]

index = 1
for name in names:
    print(f"{index}. {name}")
    index += 1
