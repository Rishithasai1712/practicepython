def sort(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])
list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort(list)
print("Sorted List:", sorted_list)
