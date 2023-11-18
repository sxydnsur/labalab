from datetime import datetime

# Task 1
def get_keys_with_value_true(input_dict):
    return [key for key, value in input_dict.items() if value is True]

def get_unique_elements(input_list):
    return [element for element in input_list if input_list.count(element) <= 1]

def get_date_in_format(date):
    day, month, year = date.split('.')
    return f"{day}.{month}.{year}"

def get_elements_with_no_more_than_two_occurrences(input_list):
    return [element for element in set(input_list) if input_list.count(element) <= 2]

def get_words_from_string(input_string):
    return input_string.split()

# Task 2
def get_unique_elements_with_count(input_list):
    return {element: input_list.count(element) for element in set(input_list)}

def get_prime_numbers(n):
    primes = [num for num in range(2, n + 1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return primes

def get_prime_numbers_in_list(input_list):
    return [num for num in input_list if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

def get_difference_between_dates(date1, date2):
    date_format = "%Y.%m.%d"
    date1 = datetime.strptime(date1, date_format)
    date2 = datetime.strptime(date2, date_format)
    difference = (date2 - date1).days
    return difference

# Task 3
def get_perfect_numbers(input_list):
    return [num for num in input_list if sum(divisor for divisor in range(1, num) if num % divisor == 0) == num]

def get_perfect_squares(input_list):
    return [num for num in input_list if int(num**0.5)**2 == num]

def sort_by_price(shopping_list):
    return sorted(shopping_list, key=lambda x: x['price'])

def get_words_starting_with_vowel(words):
    return [word for word in words if word[0].lower() in ['a', 'e', 'i', 'o', 'u']]

# Example usage
if __name__ == "__main__":
    # Task 1
    dict_input = {"a": True, "b": False, "c": True}
    print(get_keys_with_value_true(dict_input))

    list_input = [1, 2, 3, 1, 2, 4]
    print(get_unique_elements(list_input))

    date_input = "2023.10.23"
    print(get_date_in_format(date_input))

    list_input_2 = [1, 2, 3, 1, 2, 4]
    print(get_elements_with_no_more_than_two_occurrences(list_input_2))

    string_input = "This is a string with several words."
    print(get_words_from_string(string_input))

    # Task 2
    list_input_3 = [1, 2, 3, 1, 2, 4, 1, 2]
    print(get_unique_elements_with_count(list_input_3))

    n_input = 100
    print(get_prime_numbers(n_input))

    list_input_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
    print(get_prime_numbers_in_list(list_input_4))

    date1_input = "2023.10.23"
    date2_input = "2023.10.24"
    print(get_difference_between_dates(date1_input, date2_input))

    # Task 3
    binary_string_input = "10110011"
    print(get_perfect_numbers(list_input_4))

    expression_input = "4, 25, 81"
    print(get_perfect_squares(list(map(int, expression_input.split(', ')))))

    shopping_list_input = [
        {"name": "Apple", "price": 100},
        {"name": "Banana", "price": 50},
        {"name": "Orange", "price": 20}
    ]
    print(sort_by_price(shopping_list_input))

    words_input = ["apple", "banana", "orange", "bear", "cat"]
    print(get_words_starting_with_vowel(words_input))
