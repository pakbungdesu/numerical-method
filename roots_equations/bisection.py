
import equations as eq
import csv


def bisection(lower, upper, err, max_repeat):
    my_dict = eq.build_expression()
    all_data = []

    i = 0

    while i < max_repeat and abs(lower - upper) >= err:
        fa = eq.expression(my_dict, lower)
        middle = (lower + upper) / 2
        fm = eq.expression(my_dict, middle)

        this_row = [i + 1, lower, upper, middle, fa, fm]
        all_data.append(this_row)

        if fa * fm < 0:
            upper = middle
        else:
            lower = middle

        i += 1

    return all_data


# Process
a = float(input("Enter a: "))
b = float(input("Enter b: "))
error = float(input("Enter error of EPSILON: "))
max_iter = int(input("Enter max iteration: "))
print("Equation's input")
data = bisection(a, b, error, max_iter)


# Write to the CSV file
header = ["round", "a", "b", "m", "f(a)", "f(m)"]

with open('bisection_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)