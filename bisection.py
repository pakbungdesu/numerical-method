
import csv

def build_equation():
    res = {}
    more = 'y'
    while more == 'y':
        coef = input("Enter coefficient: ")
        expo = input("Enter exponent: ")

        if expo in res:
            res[expo] += coef
        else:
            res[expo] = coef

        more = input("Are there any expressions? type 'y' or 'n': ")
    return res


def equation(my_dict, x):
    res = 0
    for expo in list(my_dict.keys()):
        res += int(my_dict[expo]) * x ** int(expo)
    return res


def bisection(a, b, iterations):
    data = []
    my_dict = build_equation()

    for i in range(iterations):
        fa = equation(my_dict, a)
        m = (a + b) / 2
        fm = equation(my_dict, m)
        this_row = [i+1, a, b, m, fa, fm]
        data.append(this_row)

        if fa * fm < 0:
            b = m
        else:
            a = m

    return data


# Process
a = float(input("Enter a: "))
b = float(input("Enter b: "))
iterations = int(input("Enter iterations: "))
data = bisection(a, b, iterations)

# Write to the CSV file
header = ["round", "a", "b", "m", "f(a)", "f(m)"]

with open('bisection_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

