def find_two_sum(numbers, target_sum):
    d = {}
    for i, number in enumerate(numbers):
        key = target_sum - number
        if key in d.keys():
            print(d)
            return d[key], i
        else:
            d[key] = number

    return None


if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
