# Числа, які ми будемо використовувати для роботи з цілими числами
a = 10
b = 2

# Числа, які ми будемо використовувати для роботи з плаваючою точкою
c = 3.14
d = 2.71

# Покращена функція для виводу результату операції
def print_result(name, result, operation):
    print(f"name: {name} "
          f"/ operation: {operation}"
          f" / result: {result}")

# Робота з цілими числами
print("Робота з цілими числами:")
print_result("sum_result", a + b, "a + b")
print_result("subtraction_result", a - b, "a - b")
print_result("multiplication_result", a * b, "a * b")
print_result("division_result", a / b, "a / b")
print_result("remainder_result", a % b, "a % b")
print_result("exponentiation_result", a ** b, "a ** b")
print_result("floor_division_result", a // b, "a // b")

# Робота з плаваючою точкою
print("\nРобота з плаваючою точкою:")
print_result("float_sum_result", c + d, "c + d")
print_result("float_subtraction_result", c - d, "c - d")
print_result("float_multiplication_result", c * d, "c * d")
print_result("float_division_result", c / d, "c / d")

# Hi
