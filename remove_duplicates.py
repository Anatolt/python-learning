def remove_duplicates(spisok):
    new_spisok = []
    for i in spisok:
        if i not in new_spisok:
            new_spisok.append(i)
    return new_spisok
print remove_duplicates([1,1,2,2])
