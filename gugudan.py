print("구구단을 출력합니다.\n")
for x in range(1, 11):
    print("------- [" + str(x) + "단] -------")
    for y in range(1, 11):
        print(x, "X", y, "=", x*y)
print("---------------------")