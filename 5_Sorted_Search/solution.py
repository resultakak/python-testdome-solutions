def count_numbers(sorted_list, less_than):
    s, e = 0, len(sorted_list)
    if sorted_list[0] >= less_than:
        return s
    if sorted_list[-1] < less_than:
        return e

    while True:
        if s >= e:
            return 0

        if s < 0 or e > len(sorted_list):
            return 0

        pivot = (s + e) // 2
        if sorted_list[pivot] < less_than:
            if sorted_list[pivot + 1] >= less_than:
                return pivot + 1
            else:
                s = pivot
        elif sorted_list[pivot] >= less_than:
            e = pivot


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4))  # should print 2
