from give_bmi import give_bmi, apply_limit


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    print("\n------------invalid value---------------")
    bmi = give_bmi([1.68, 'a'], [165.3, 38.4])
    print(bmi, type(bmi))

    print("\n------------unequal length---------------")
    bmi = give_bmi([1.68, 1.7, 1.8], [165.3, 38.4])
    print(bmi, type(bmi))
    print(apply_limit(bmi, 'aa'))


if __name__ == "__main__":
    main()
