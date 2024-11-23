def generate_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    sequence.append(1)
    return sequence

cache={}
def generate_sequence_with_cache(n):
    original_n = n
    sequence = []

    while n != 1:
        if n in cache:
            sequence.extend(cache[n])
            break
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    else:
        sequence.append(1)
    for i in range(len(sequence)):
        if sequence[i] not in cache:
            cache[sequence[i]] = sequence[i:]
    return sequence



#without cache
result_3=generate_sequence(3)
result_10=generate_sequence(10)
print(result_3)
print(result_10)
#with cache
result_with_cache_3=generate_sequence_with_cache(3)
result_with_cache_10=generate_sequence_with_cache(10)
print(result_with_cache_3)
print(result_with_cache_10)