def is_even(number):
    return not bool(number % 2)

result= is_even(int(input("nombre ?")))
print(result)