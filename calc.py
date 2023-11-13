history = {
    "+": [],
    "-": [],
    "*": [],
    "/": []
}
while True:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Введите операцию: ")
    result = None
    if operation == '+':
        result = a+b
    elif operation == '-':
        result = a-b
    elif operation == '*':
        result = a*b
    elif operation == '/':
        if b == 0:
            print("На ноль делить нельзя!")
        else:
            result = a/b
    else:
        print("Такой операции нет")

    history[operation].append(f"{a}{operation}{b}={result}")

    for key, value in history.items():
        print(key, value)
