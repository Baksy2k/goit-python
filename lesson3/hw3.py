def main():
    a = 1
    while a:
        n = int(input("Введите положительное целое число: "))
        if n<=0:
            print("Введите не отрицательное число и не ноль")
        else:
            break
    return n

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

if __name__ == '__main__':
    n = main()
    print(f"{n}-й член ряда фибоначчи равен: {fibonacci(n)}")