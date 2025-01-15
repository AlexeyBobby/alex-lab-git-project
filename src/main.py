from src.utils import add_numbers

if __name__ == "__main__":
    result = add_numbers(5, 3)
    print(f"The result of adding 5 and 3 is {result}")

from src.utils import add_numbers, multiply_numbers

if __name__ == "__main__":
    result_add = add_numbers(5, 3)
    result_multiply = multiply_numbers(5, 3)
    print(f"The result of adding 5 and 3 is {result_add}")
    print(f"The result of multiplying 5 and 3 is {result_multiply}")