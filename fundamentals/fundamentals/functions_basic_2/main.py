def countdown(num):
    numbers = []
    while num >= 0:
        numbers.append(num)
        num -= 1
    return numbers

def print_and_return(numbers):
    if len(numbers) == 2:
        print(numbers[0])
        return numbers[1]
    else:
        return False

def first_plus_length(numbers):
    list_len = len(numbers)
    return (list_len + 1)

def greater_than_second(numbers):
    if len(numbers) < 2:
        return False
    else:
        second_num = numbers[1]
        greater = []

        for i in range(0, len(numbers)):
            if numbers[i] > second_num:
                greater.append(numbers[i])

        return greater

def length_and_value(length, num):
    num_list = []
    for i in range(0, length):
        num_list.append(num)

    return num_list

if __name__ == '__main__':
    print(countdown(20))
    print(print_and_return([1,2]))
    print(first_plus_length([1, 2, 3]))
    print(greater_than_second([5, 2, 3, 2, 1, 4]))
    print(length_and_value(6, 2))