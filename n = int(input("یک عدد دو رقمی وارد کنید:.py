n = int(input("یک عدد دو رقمی وارد کنید: "))
if 10 <= n <= 99:
    a = n // 10
        b = n % 10
            print(f"{a}^{b} =", a ** b)
                print(f"{b}^{a} =", b ** a)
                else:
                    print("خطا: عدد وارد شده دو رقمی نیست")