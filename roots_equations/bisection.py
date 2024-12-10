
from expression import *
import csv


def bisection(lower, upper, err, max_repeat):
    all_data = []
    print("Equation's input")
    expr = build_expression()
    if expr.evaluate(lower) * expr.evaluate(upper) >= 0:
        print("You have not assumed right a and b")
        return all_data

    i = 0
    while i < max_repeat and abs(lower - upper) >= err:
        fa = expr.evaluate(lower)
        middle = (lower + upper) / 2
        fm = expr.evaluate(middle)

        this_row = [i + 1, lower, upper, middle, fa, fm]
        all_data.append(this_row)

        if fa * fm < 0:
            upper = middle
        elif fa * fm > 0:
            lower = middle
        else:
            break
        i += 1
    return all_data


# Process
a = float(input("Enter a: "))
b = float(input("Enter b: "))
error = float(input("Enter error tolerance: "))
max_iter = int(input("Enter max iteration: "))
data = bisection(a, b, error, max_iter)


if data != []:
    # Write to the CSV file
    header = ["round", "a", "b", "m", "f(a)", "f(m)"]

    with open('bisection_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
else:
    print("Program stops because f(a) * f(b) >= 0")
