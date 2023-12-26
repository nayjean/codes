data = []

for _ in range(5):
    name = input("Enter a name: ")
    number = int(input("Enter a number: "))
    data.append([name, number])

result_dict = {}
for pair in data:
    result_dict[pair[0]] = pair[1]

sorted_dict = dict(sorted(result_dict.items(), key=lambda item: item[1]))

print(sorted_dict)
