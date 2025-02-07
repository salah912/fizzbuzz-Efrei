def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Erreur"  # 🚨 Bug volontaire, au lieu de "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
