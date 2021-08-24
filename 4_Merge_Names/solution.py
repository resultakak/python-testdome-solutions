from itertools import chain


def unique_names(names1, names2):
    return list(set(chain(names1 + names2)))


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia
