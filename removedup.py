list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
result = []
seen = set()
for item in list:
    if item not in seen:
        result.append(item)
        seen.add(item)
print("Resulting List:", result)
