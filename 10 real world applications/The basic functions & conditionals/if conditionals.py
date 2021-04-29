def mean(values):
    if type(values) == dict:
        the_mean = sum(values.values()) / len(values)
    else:    
        the_mean = sum(values) / len(values)
    return the_mean

students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(students_grades))    