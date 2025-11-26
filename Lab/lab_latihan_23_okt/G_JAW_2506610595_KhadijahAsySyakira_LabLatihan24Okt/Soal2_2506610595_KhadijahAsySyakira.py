def who_above_avg(lst_students):
    names, values = [], []
    for x in lst_students:
        nama = x[0]
        nilai = x[1]
        names.append(nama)
        values.append(nilai)
    
    avg = sum(values)/len(names)
    
    names_above = []
    for y in lst_students:
        if y[1] >= avg:
            names_above.append(y[0])

    return names_above
