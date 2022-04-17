# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import copy


def coerce_at_least(value, min_value):
    return value if value >= min_value else min_value


class Polynomial:
    # Буква, которая используется в выводе
    POLYNOMIAL_LETTER = 'x'

    # Инициализируем полином.
    # Элемент self.factors имеет вид [коеффициет, степень] [3,2] -> 3x^2
    # Список self.factors имеет вид [[5, 2], [3, 2], [-4, 2]] -> 5x^2 + 3x^2 - 4x^2
    def __init__(self, *_factors):
        # Содержит коеффициенты и степени всех многочленов
        self.factors = []
        self.factors.extend(_factors)

    def add_poly(self, other):
        new_factors = []
        new_factors.extend(self.factors)

        for factor in other.factors:
            self.__add_factor(_factors=new_factors, factor=factor)

        new_factors.sort(key=lambda x: x[1], reverse=True)
        new_factors = self.__clear_from_empty_factors(new_factors)

        self.factors = new_factors

    @staticmethod
    def __add_factor(_factors, factor):
        degree = factor[1]
        for i in range(len(_factors)):
            if _factors[i][1] == degree:
                _factors[i][0] += factor[0]
                return

        _factors.append(factor)

    @staticmethod
    def __clear_from_empty_factors(factors):
        new_factors = []
        for factor in factors:
            if factor[0] != 0:
                new_factors.append(factor)

        return new_factors

    def multiply_poly(self, other):
        new_factors = []
        for i in self.factors:
            for j in other.factors:
                factor = [i[0] * j[0], i[1] + j[1]]
                new_factors.append(factor)

        new_factors.sort(key=lambda x: x[1], reverse=True)

        new_factors = self.__normalize(new_factors)

        self.factors = new_factors

    # Текущая реализвация сложения двух полиномов нормализует выражение
    @staticmethod
    def __normalize(factors):
        empty_poly = Polynomial()
        new_poly = Polynomial(*factors)

        empty_poly.add_poly(new_poly)

        return empty_poly.factors

    # Находит производную. Используется правило: (a^n)' = na^(n-1)
    def derivative(self):
        new_factors = []
        for i in range(len(self.factors)):
            factor = []

            coef = self.factors[i][0]
            degree = self.factors[i][1]

            factor.append(coef * degree)
            factor.append(coerce_at_least(degree - 1, 0))

            new_factors.append(factor)

        return Polynomial(*new_factors)

    def __str__(self):
        poly_with_letters = []
        for x in range(len(self.factors)):
            curr_letter = self.POLYNOMIAL_LETTER if self.factors[x][1] > 0 else ''
            curr_degree_str = "^" + str(self.factors[x][1]) if self.factors[x][1] > 1 else ''
            if x == 0 and self.factors[0][0] != 0:
                poly_with_letters.append(str(self.factors[x][0]) + curr_letter + curr_degree_str)
            else:
                if self.factors[x][0] > 0:
                    poly_with_letters.append('+ ' + str(self.factors[x][0]) + curr_letter + curr_degree_str)
                elif self.factors[x][0] < 0:
                    poly_with_letters.append(
                        '- ' + str(self.factors[x][0]).replace('-', '') + curr_letter + curr_degree_str)

        if len(poly_with_letters) == 0:
            return "Empty polynomial"
        else:
            if poly_with_letters[0][0] == '-':
                poly_with_letters[0] = poly_with_letters[0].replace(" ", "")
            else:
                poly_with_letters[0] = poly_with_letters[0].replace("+ ", "")

            return " ".join(poly_with_letters)


class TestManager:
    TEST_PASSED_STRING = "Passed"
    TEST_FAILED_STRING = "Failed"

    def __init__(self):
        self.tests = []

    def add_test(self, test_name, test):
        self.tests.append([test_name, test])

    def run_all_tests(self):
        for test in self.tests:
            self.check_test(test[0], test[1])

    def check_test(self, test_name, test):
        print(test_name + ": " + (self.TEST_PASSED_STRING if test() else self.TEST_FAILED_STRING))


def test_sum():
    test_poly1 = Polynomial([-3, 3], [4, 2], [-5, 1])
    test_poly2 = Polynomial([3, 3], [4, 2], [-5, 1], [4, 4])

    test_poly1.add_poly(test_poly2)

    expected_result = [[4, 4], [8, 2], [-10, 1]]

    return test_poly1.factors == expected_result


def test_mul():
    test_poly1 = Polynomial([-3, 3], [4, 2], [-5, 1])
    test_poly2 = Polynomial([3, 3], [4, 2], [-5, 1], [4, 4])

    test_poly1.multiply_poly(test_poly2)

    expected_result = [[-12, 7], [7, 6], [-20, 5], [16, 4], [-40, 3], [25, 2]]

    return test_poly1.factors == expected_result


def test_derivative():
    test_poly = Polynomial([-3, 3], [4, 2], [-5, 1])

    result_poly = test_poly.derivative()

    expected_result = [[-9, 2], [8, 1], [-5, 0]]

    return result_poly.factors == expected_result


def test_str():
    test_poly = Polynomial([-3, 3], [4, 2], [-5, 1])

    result_str = str(test_poly)

    expected_result = "-3x^3 + 4x^2 - 5x"

    return result_str == expected_result


def run_gui():
    first_poly_factors = []
    print("Введите степень первого полинома:")
    curr_poly_degree = int(input())
    for i in range(curr_poly_degree, -1, -1):
        print("Введите коэффициент для x^" + str(i))
        coef = int(input())
        first_poly_factors.append([coef, i])

    second_poly_factors = []
    print("Введите степень второго полинома:")
    curr_poly_degree = int(input())
    for i in range(curr_poly_degree, -1, -1):
        print("Введите коэффициент для x^" + str(i))
        coef = int(input())
        second_poly_factors.append([coef, i])

    first_poly = Polynomial(*first_poly_factors)
    second_poly = Polynomial(*second_poly_factors)

    while True:
        user_choose = 0
        print("(1) Вывести сумму")
        print("(2) Вывести произведение")
        print("(3) Вывести оба полинома")
        print("(4) Выход")
        user_choose = int(input())
        if not (0 < user_choose < 5):
            print("Введено неккоректное число")
            break

        if user_choose == 1:
            new_poly = copy.deepcopy(first_poly)
            new_poly.add_poly(second_poly)
            print(new_poly)
        elif user_choose == 2:
            new_poly = copy.deepcopy(first_poly)
            new_poly.multiply_poly(second_poly)
            print(new_poly)
        elif user_choose == 3:
            print("Первый полином: ", first_poly)
            print("Второй полином: ", second_poly)
        elif user_choose == 4:
            print("Бывай.")
            return


def run_tests():
    test_manager = TestManager()

    test_manager.add_test("Test sum", test_sum)
    test_manager.add_test("Test mul", test_mul)
    test_manager.add_test("Test derivative", test_derivative)

    test_manager.run_all_tests()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # run_tests()

    run_gui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
