
import math

class Term:
    def __init__(self, coef, expo, func):
        self.coef = coef
        self.expo = expo
        self.func = func

    def calculate(self, x):
        if self.func == "x":
            return self.coef * x ** self.expo
        elif self.func == "sin":
            return self.coef * math.sin(x) ** self.expo
        elif self.func == "cos":
            return self.coef * math.cos(x) ** self.expo
        else:
            return self.coef * math.exp(x)


class Expression:
    def __init__(self):
        self.terms = []

    def add_term(self, term):
        self.terms.append(term)

    def evaluate(self, x):
        res = 0
        for ele in self.terms:
            res += ele.calculate(x)
        return res


def build_expression():
    more = "y"
    func = ["x", "sin", "cos", "exp"]
    expr = Expression()

    while more == "y":
        coef = int(input("Insert coefficient: "))
        expo = int(input("Insert exponent: "))
        print("1 - x variable\n2 - sin\n3 - cos\n4 - euler's number")
        choice = int(input("Select type of this expression. Enter 1-4: "))


        expr.add_term(Term(coef, expo, func[choice-1]))
        more = str(input("Are there any expressions? type 'y' or 'n': "))

    return expr


# Test
# expr = Expression()
# expr.add_term(Term(2, 3, "x"))
# expr.add_term(Term(-1, 2, "sin"))
# expr.add_term(Term(0.5, 1, "exp"))
#
# result = expr.evaluate(3.71875)
# print(result)
