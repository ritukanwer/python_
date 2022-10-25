def find_even_numbers(lst):
    evens = []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
    return evens


def length_of_dictionary(ages):
    length = len(ages)
    return length



def average_of_students(ages):
    total = 0
    for i in ages:
                total += i
    return total
age_students = average_of_students(ages.values())
total = average_of_students(age_students)
average_age = total / len(age_students)


def oldest_student(students):
	return max(students, key=students.get)

