# Checking for a palindrome
def check_for_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


# Converting foo to base b and returning
def convert_to_base(foo, b):
    numbers = []
    while foo > 0:
        numbers.append(str(foo % b))
        foo /= b
    numbers = numbers[::-1]
    numbers = ''.join(numbers)
    return int(numbers)


# Checking each base for palindromes until one is found
new_number = 0  # couldn't figure out a better way to do this without a global variable


def answer(n):
    global new_number
    if n == 0:
        return 2
    check_condition = False
    m = 1
    while check_condition == False:
        m += 1
        if check_for_palindrome(convert_to_base(n, m)) is True:
            new_number = convert_to_base(n, m)
            return m
            break

# Prints the lowest base you can convert the inputted number(base 10) to in order to achieve a palindrome
final = raw_input("Your number: ")
print "base:", answer(int(final)), "number:", new_number
