def find_even_numbers(lst):
    evens = []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
    return evens
