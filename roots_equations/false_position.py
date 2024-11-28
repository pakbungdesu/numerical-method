
import csv
import equations as eq

def falsepos(lower, upper, error_tol, max_iters):

    all_data = []
    print("Equation's input")
    my_dict = eq.build_expression()
    if eq.expression(my_dict, lower) * eq.expression(my_dict, upper) >= 0:
        print("You have not assumed right a and b")
        return all_data

    i = 0
    prev_c = None
    while i < max_iters:

        fa = eq.expression(my_dict, lower)
        fb = eq.expression(my_dict, upper)
        c = ((upper * fa - lower * fb) / (fa - fb))
        fc = eq.expression(my_dict, c)

        this_row = [i+1, lower, upper, fa, fb, c, fc]
        all_data.append(this_row)

        # Check for convergence
        if prev_c is not None and abs(c - prev_c) < error_tol:
            break

        if fa * fc > 0:
            lower = c
        elif fa * fc < 0:
            upper = c
        else:
            break

        prev_c = c
        i += 1

    return all_data


# Process
a = float(input("Enter a: "))
b = float(input("Enter b: "))
error = float(input("Enter error tolerance: "))
iters = int(input("Enter max iteration: "))
data = falsepos(a, b, error, iters)


if data != []:
    # Write to the CSV file
    header = ["round", "a", "b", "f(a)", "f(b)", "c", "f(c)"]

    with open('falsepos_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
else:
    print("Program stops because f(a) * f(b) >= 0")
