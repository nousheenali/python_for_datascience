def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    #bmi = wieght / height ** 2
    for i in height:
        print(i)
        # for j in weight:
        #     bmi = j / i ** 2
        #     return bmi


# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#     #your code here

l1 = [1.78, 1.60, 1.65]
l2 = [70, 60, 65]
give_bmi(l1, l2)