
import math

def build_expression():
    res = {'x': [], 'sin': [], 'cos': [], 'exp': []}
    more = 'y'
    while more == 'y':
        coef = int(input("Enter coefficient: "))
        expo = int(input("Enter exponent: "))
        print("1 - x variable\n2 - sin\n3 - cos\n4 - euler's number")
        choice = int(input("Select type of this expression. Enter 1-4: "))

        if choice == 1:
            res['x'].append((coef, expo))
        elif choice == 2:
            res['sin'].append((coef, expo))
        elif choice == 3:
            res['cos'].append((coef, expo))
        else:
            res['exp'].append((coef, expo))

        more = input("Are there any expressions? type 'y' or 'n': ")

    return res


def expression(my_dict, x):
    res = 0
    for key in my_dict:
        for ele in list(my_dict[key]):
            if key == 'x':
                res += ele[0] * x ** ele[1]
            elif key == 'sin':
                res += ele[0] * math.sin(x) ** ele[1]
            elif key == 'cos':
                res += ele[0] * math.cos(x) ** ele[1]
            else:
                x = x ** ele[1]
                res += ele[0] * math.exp(x)
    return res


# my_dict = build_expression()
# res = expression(my_dict, 3.71875)
# print(res)
