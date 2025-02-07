def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "ERROR"  # Introduit volontairement un bug
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
