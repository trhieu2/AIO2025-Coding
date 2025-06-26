def compute_f1_score(tp, fp, fn):
    inputs = [tp, fp, fn]

    for val in inputs:
        try:
            int(val)
        except ValueError:
            print(f"'{val}' is NOT an integer.")
            return

    for val in inputs:
        if val < 0:
            print(f"'{val}' is smaller than 0")
            return

    try:
        precision = tp/(tp+fp)
    except ZeroDivisionError:
        print("Error: Division by zero")

    try:
        recall = tp/(tp+fn)
    except ZeroDivisionError:
        print("Error: Division by zero")

    return (2*precision*recall)/(precision+recall)


print(compute_f1_score(2,3,4))
print(compute_f1_score('a',3,4))


