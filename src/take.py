def take(sequence, number):
    i = 0
    while i < number:
        yield sequence[i]
        i += 1
