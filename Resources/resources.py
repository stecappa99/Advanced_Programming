resource = 0

def count_res(f):
    f.__dict__["cont"] = 0

    def inner(*args):
        f.__dict__["cont"] += 1
        if f.__dict__["cont"] <= resource:
            val = f(*args)
            f.__dict__["cont"] = 0

            return val
        else:
            f.__dict__["cont"] = 0
            print("resources run out")
            raise SystemExit
    return inner

@count_res
def fact(val):
    return 1 if val <= 1 else val * fact(val-1)

if __name__ == "__main__":
    resource = 10
    print("{0}! :- {1}".format(10, fact(10)))
    resource = 9
    try:
        print("{0}! :- {1}".format(10, fact(10)))
    except SystemExit:
        pass
