def isThisPartOfFibonacci(wantedValue):
    previousValue = 0
    nextValue = 1

    fibo = 0
    allInOneLine = ""
    while fibo < wantedValue:
        fibo = previousValue + nextValue
        previousValue = nextValue
        nextValue = fibo
    return f"{wantedValue} faz parte da sequência de fibonacci" if fibo == wantedValue else f"{wantedValue} não faz parte da sequência de fibonacci"

wantedValue = int(input("Insert value"))
print(isThisPartOfFibonacci(wantedValue))
