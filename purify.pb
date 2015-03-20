# progrmm del odd numbers from array
def purify(numbers):
    new_numbers = []
    for n in numbers:
        if n%2 == 0:
            new_numbers.append(n)
    return new_numbers

print purify([1,2,3]) # 2
