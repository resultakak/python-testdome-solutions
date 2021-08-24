class Problem:

    @staticmethod
    def foobar(n):
        r = []
        for i in range(n):
            i += 1
            if i % 3 == 0 and i % 5 == 0:
                e = "foobar"
            elif (i % 3 == 0):
                e = "foo"
            elif (i % 5 == 0):
                e = "bar"
            else:
                e = str(i)

            r.append(e)
        return r


print('\n'.join(Problem.foobar(8)))
