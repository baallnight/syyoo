from calc.Calc import Calc


def main():
    calc = Calc(1, 2)
    calc.set_num(3, 6)
    print("{} + {} = {}".format(calc.first,
                                calc.second,
                                calc.sum()))

# main()

if __name__ == '__main__':
    main()