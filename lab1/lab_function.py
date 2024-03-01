def count_digits(num):
    res = 0
    if 0 <= num <= 9:
        res += 1
    else:
        while num > 1:
            res += 1
            num /= 10
    return res
